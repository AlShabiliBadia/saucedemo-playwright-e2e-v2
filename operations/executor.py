from playwright.sync_api import Page
from operations.models.pipeline_data import TestPipeline, Operation
from operations.operations import base_ops
from operations.operations import login_ops
from operations.operations import inventory_ops
from operations.operations import cart_checkout_ops


OPERATION_REGISTRY = {
    "navigate": base_ops.op_navigate,
    "fill": base_ops.op_fill,
    "click": base_ops.op_click,
    "verify_text": base_ops.op_verify_text,
    "verify_url": base_ops.op_verify_url,
    "verify_visible": base_ops.op_verify_visible,
    
    "login": login_ops.op_login,
    "assert_login_success": login_ops.op_assert_login_success,
    "assert_login_failure": login_ops.op_assert_login_failure,

    "sort_products": inventory_ops.op_sort_products,
    "add_item_to_cart": inventory_ops.op_add_item_to_cart,
    "assert_product_names": inventory_ops.op_assert_product_names,
    "assert_product_prices": inventory_ops.op_assert_product_prices,
    "assert_remove_button_visible": inventory_ops.op_assert_remove_button_visible,

    "go_to_cart": cart_checkout_ops.op_go_to_cart,
    "assert_cart_badge_count": cart_checkout_ops.op_assert_cart_badge_count,
    "assert_item_in_cart": cart_checkout_ops.op_assert_item_in_cart,
    "go_to_checkout_step_one": cart_checkout_ops.op_go_to_checkout_step_one,
    "fill_checkout_info": cart_checkout_ops.op_fill_checkout_info,
    "go_to_checkout_step_two": cart_checkout_ops.op_go_to_checkout_step_two,
    "assert_item_in_overview": cart_checkout_ops.op_assert_item_in_overview,
    "finish_checkout": cart_checkout_ops.op_finish_checkout,
    "assert_order_complete": cart_checkout_ops.op_assert_order_complete,
}

class PipelineExecutor:
    def __init__(self, page: Page):
        self.page = page

    def run_pipeline(self, pipeline: TestPipeline):
        for op_model in pipeline.operations:
            self._execute_operation(op_model)

    def _execute_operation(self, op_model: Operation):
        op_name = op_model.name
        
        op_func = OPERATION_REGISTRY.get(op_name)
        
        if not op_func:
            raise ValueError(f"Unknown operation: {op_name}")

        op_args = op_model.model_dump(exclude={"name"})
        
        op_func(self.page, **op_args)