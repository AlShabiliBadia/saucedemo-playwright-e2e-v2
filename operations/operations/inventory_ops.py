from playwright.sync_api import Page, expect


SORT_CONTAINER = "[data-test='product-sort-container']"
INVENTORY_ITEM = ".inventory_item"
ITEM_NAME = ".inventory_item_name"
ITEM_PRICE = ".inventory_item_price"
CART_BADGE = ".shopping_cart_badge"

def op_sort_products(page: Page, sort_order: str):
    page.locator(SORT_CONTAINER).select_option(sort_order)

def op_add_item_to_cart(page: Page, item_name: str):
    item_container = page.locator(INVENTORY_ITEM).filter(has_text=item_name)
    add_button = item_container.locator("button[id^='add-to-cart-']")
    add_button.click()

def op_assert_product_names(page: Page, expected_names: list[str]):
    actual_names = page.locator(ITEM_NAME).all_text_contents()
    assert actual_names == expected_names, f"Product names mismatch. Got: {actual_names}"

def op_assert_product_prices(page: Page, expected_prices: list[float]):
    price_texts = page.locator(ITEM_PRICE).all_text_contents()
    actual_prices = [float(price.replace("$", "")) for price in price_texts]
    assert actual_prices == expected_prices, f"Product prices mismatch. Got: {actual_prices}"

def op_assert_remove_button_visible(page: Page, item_name: str):
    item_container = page.locator(INVENTORY_ITEM).filter(has_text=item_name)
    remove_button = item_container.locator("button[id^='remove-']")
    expect(remove_button).to_be_visible()
    expect(remove_button).to_have_text("Remove")