from playwright.sync_api import Page, expect
from typing import Optional

LOGIN_URL = "https://www.saucedemo.com/"
USERNAME_INPUT = "[data-test='username']"
PASSWORD_INPUT = "[data-test='password']"
LOGIN_BUTTON = "[data-test='login-button']"
ERROR_MESSAGE = "[data-test='error']"
INVENTORY_URL = "https://www.saucedemo.com/inventory.html"

def op_login(page: Page, username: Optional[str] = None, password: Optional[str] = None):
    page.goto(LOGIN_URL)
    
    if username is not None:
        page.locator(USERNAME_INPUT).fill(username)
    if password is not None:
        page.locator(PASSWORD_INPUT).fill(password)
        
    page.locator(LOGIN_BUTTON).click()

def op_assert_login_success(page: Page):
    expect(page).to_have_url(INVENTORY_URL)

def op_assert_login_failure(page: Page, expected_error: str):
    expect(page.locator(ERROR_MESSAGE)).to_be_visible()
    expect(page.locator(ERROR_MESSAGE)).to_have_text(expected_error)