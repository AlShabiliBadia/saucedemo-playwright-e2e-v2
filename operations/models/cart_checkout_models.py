from pydantic import BaseModel, Field
from typing import List, Literal, Annotated

class GoToCart(BaseModel):
    name: Literal["go_to_cart"] = "go_to_cart"

class AssertCartBadgeCount(BaseModel):
    name: Literal["assert_cart_badge_count"] = "assert_cart_badge_count"
    count: int

class AssertItemInCart(BaseModel):
    name: Literal["assert_item_in_cart"] = "assert_item_in_cart"
    item_name: Annotated[str, Field(min_length=1)]

class GoToCheckoutStepOne(BaseModel):
    name: Literal["go_to_checkout_step_one"] = "go_to_checkout_step_one"

class FillCheckoutInfo(BaseModel):
    name: Literal["fill_checkout_info"] = "fill_checkout_info"
    first_name: str
    last_name: str
    postal_code: str

class GoToCheckoutStepTwo(BaseModel):
    name: Literal["go_to_checkout_step_two"] = "go_to_checkout_step_two"

class AssertItemInOverview(BaseModel):
    name: Literal["assert_item_in_overview"] = "assert_item_in_overview"
    item_name: Annotated[str, Field(min_length=1)]

class FinishCheckout(BaseModel):
    name: Literal["finish_checkout"] = "finish_checkout"

class AssertOrderComplete(BaseModel):
    name: Literal["assert_order_complete"] = "assert_order_complete"
    expected_message: Annotated[str, Field(min_length=1)]