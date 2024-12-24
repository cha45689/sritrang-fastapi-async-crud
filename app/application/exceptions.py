"""
This module is use to host custome exception handler code
"""

from fastapi import Request
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import RequestValidationError
from starlette.responses import JSONResponse


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
