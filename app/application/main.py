"""
This Module is use to declare and bundle the main FastAPI application
"""

from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError

from app.application.exceptions import validation_exception_handler
from app.application.routers.routes import routers
from app.database.connection.sqlite import register_sqlite


@asynccontextmanager
async def lifespan(app: FastAPI):  # pylint: disable=W0621
    """
    lifespan method use run setup and teardown process
    """
    async with register_sqlite(app):
        yield


app = FastAPI(lifespan=lifespan)

app.include_router(routers)

app.add_exception_handler(RequestValidationError, validation_exception_handler)
