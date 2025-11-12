from pydantic import BaseModel, Field
from typing import List, Literal, Union, Optional
from typing_extensions import Annotated

class Navigate(BaseModel):
    name: Literal["navigate"] = "navigate"
    url: Annotated[str, Field(min_length=1)]

class Fill(BaseModel):
    name: Literal["fill"] = "fill"
    selector: Annotated[str, Field(min_length=1)]
    value: str

class Click(BaseModel):
    name: Literal["click"] = "click"
    selector: Annotated[str, Field(min_length=1)]

class VerifyText(BaseModel):
    name: Literal["verify_text"] = "verify_text"
    selector: Annotated[str, Field(min_length=1)]
    expected_text: Annotated[str, Field(min_length=1)]

class VerifyURL(BaseModel):
    name: Literal["verify_url"] = "verify_url"
    expected_url: Annotated[str, Field(min_length=1)]

class VerifyVisible(BaseModel):
    name: Literal["verify_visible"] = "verify_visible"
    selector: Annotated[str, Field(min_length=1)]


class Login(BaseModel):
    name: Literal["login"] = "login"
    username: Optional[str] = None
    password: Optional[str] = None

class AssertLoginSuccess(BaseModel):
    name: Literal["assert_login_success"] = "assert_login_success"

class AssertLoginFailure(BaseModel):
    name: Literal["assert_login_failure"] = "assert_login_failure"
    expected_error: Annotated[str, Field(min_length=1)]