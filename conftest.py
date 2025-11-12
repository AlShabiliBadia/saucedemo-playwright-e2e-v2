import pytest
from playwright.sync_api import Page, expect

@pytest.fixture(scope="function", autouse=True)
def set_up_trace(page: Page, request: pytest.FixtureRequest):

    page.context.tracing.start(
        name=request.node.name,
        screenshots=True,
        snapshots=True,
        sources=True
    )

    yield

    test_failed = request.node.rep_call.failed

    if test_failed:
        trace_path = f"test-results/{request.node.name}-trace.zip"
        page.context.tracing.stop(path=trace_path)
    else:
        page.context.tracing.stop()

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    
    if rep.when == "call":
        item.rep_call = rep