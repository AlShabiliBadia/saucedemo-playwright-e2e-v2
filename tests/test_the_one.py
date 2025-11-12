import pytest
from playwright.sync_api import Page
from operations.executor import PipelineExecutor
from operations.models.pipeline_data import TestPipeline
from .Utility import load_pipelines

@pytest.mark.parametrize("pipeline", load_pipelines())
def test_pipeline_runner(page: Page, pipeline: TestPipeline):
    
    executor = PipelineExecutor(page)
    
    try:
        executor.run_pipeline(pipeline)
    except Exception as e:
        pytest.fail(f"Pipeline '{pipeline.test_id}' failed: {e}")