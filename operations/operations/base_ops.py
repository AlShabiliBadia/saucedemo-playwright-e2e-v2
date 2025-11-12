from playwright.sync_api import Page, expect

def op_navigate(page: Page, url: str):
    page.goto(url)

def op_fill(page: Page, selector: str, value: str):
    page.locator(selector).fill(value)

def op_click(page: Page, selector: str):
    page.locator(selector).click()

def op_verify_text(page: Page, selector: str, expected_text: str):
    expect(page.locator(selector)).to_have_text(expected_text)

def op_verify_url(page: Page, expected_url: str):
    expect(page).to_have_url(expected_url)

def op_verify_visible(page: Page, selector: str):
    expect(page.locator(selector)).to_be_visible()