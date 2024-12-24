"""
This module is use to host custome exception handler code
"""

from fastapi import Request
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import RequestValidationError
from pydantic import BaseModel
from starlette.responses import JSONResponse


class DefaultHTTPExceptionContent(BaseModel):
    """
    default htpp exception content format
    """

    detail: str = ""


async def validation_exception_handler(
    request: Request, exc: RequestValidationError  # pylint: disable=W0613
) -> JSONResponse:
    """
    custom function use to handle RequestValidationError and return 400 instead of 422
    copy from default one
    """
    return JSONResponse(
        status_code=400,
        content={"detail": jsonable_encoder(exc.errors())},
    )
