from playwright.sync_api import Page, expect
from typing import Optional

CART_LINK = ".shopping_cart_link"
CART_BADGE = ".shopping_cart_badge"
ITEM_NAME = ".inventory_item_name"
CHECKOUT_BUTTON = "[data-test='checkout']"
FIRST_NAME_INPUT = "[data-test='firstName']"
LAST_NAME_INPUT = "[data-test='lastName']"
POSTAL_CODE_INPUT = "[data-test='postalCode']"
CONTINUE_BUTTON = "[data-test='continue']"
FINISH_BUTTON = "[data-test='finish']"
COMPLETE_HEADER = ".complete-header"

def op_go_to_cart(page: Page):
    page.locator(CART_LINK).click()
    expect(page).to_have_url("https://www.saucedemo.com/cart.html")

def op_assert_cart_badge_count(page: Page, count: int):
    expect(page.locator(CART_BADGE)).to_have_text(str(count))

def op_assert_item_in_cart(page: Page, item_name: str):
    item_container = page.locator(".cart_item").filter(has_text=item_name)
    expect(item_container).to_be_visible()
    expect(item_container.locator(ITEM_NAME)).to_have_text(item_name)

def op_go_to_checkout_step_one(page: Page):
    page.locator(CHECKOUT_BUTTON).click()
    expect(page).to_have_url("https://www.saucedemo.com/checkout-step-one.html")

def op_fill_checkout_info(page: Page, first_name: str, last_name: str, postal_code: str):
    page.locator(FIRST_NAME_INPUT).fill(first_name)
    page.locator(LAST_NAME_INPUT).fill(last_name)
    page.locator(POSTAL_CODE_INPUT).fill(postal_code)

def op_go_to_checkout_step_two(page: Page):
    page.locator(CONTINUE_BUTTON).click()
    expect(page).to_have_url("https://www.saucedemo.com/checkout-step-two.html")

def op_assert_item_in_overview(page: Page, item_name: str):
    item_container = page.locator(".cart_item").filter(has_text=item_name)
    expect(item_container).to_be_visible()

def op_finish_checkout(page: Page):
    page.locator(FINISH_BUTTON).click()

def op_assert_order_complete(page: Page, expected_message: str):
    expect(page).to_have_url("https://www.saucedemo.com/checkout-complete.html")
    expect(page.locator(COMPLETE_HEADER)).to_have_text(expected_message)