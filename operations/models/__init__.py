from pydantic import BaseModel, Field
from typing import List, Literal, Union, Optional, Annotated
from .login_models import *
from .inventory_models import *
from .cart_checkout_models import *

Operation = Annotated[
    Union[
        Navigate, Fill, Click, VerifyText, VerifyURL, VerifyVisible,
        
        Login, AssertLoginSuccess, AssertLoginFailure,

        SortProducts, AddItemToCart, AssertProductNames,
        AssertProductPrices, AssertRemoveButtonVisible,

        GoToCart, AssertCartBadgeCount, AssertItemInCart, GoToCheckoutStepOne,
        FillCheckoutInfo, GoToCheckoutStepTwo, AssertItemInOverview,
        FinishCheckout, AssertOrderComplete
    ],
    Field(discriminator="name")
]