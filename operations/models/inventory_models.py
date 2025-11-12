from pydantic import BaseModel, Field
from typing import List, Literal, Annotated

class SortProducts(BaseModel):
    name: Literal["sort_products"] = "sort_products"
    sort_order: Annotated[str, Field(min_length=2)]

class AddItemToCart(BaseModel):
    name: Literal["add_item_to_cart"] = "add_item_to_cart"
    item_name: Annotated[str, Field(min_length=1)]

class AssertProductNames(BaseModel):
    name: Literal["assert_product_names"] = "assert_product_names"
    expected_names: List[str]

class AssertProductPrices(BaseModel):
    name: Literal["assert_product_prices"] = "assert_product_prices"
    expected_prices: List[float]

class AssertRemoveButtonVisible(BaseModel):
    name: Literal["assert_remove_button_visible"] = "assert_remove_button_visible"
    item_name: Annotated[str, Field(min_length=1)]