"""
This Module is use to declare and bundle the main FastAPI application
"""

from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError
from fastapi.openapi.utils import get_openapi

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


def custom_openapi(app: FastAPI) -> FastAPI:  # pylint: disable=W0621
    """
    This function is use to overwrite default status code  422 response to 400 in openapi (swagger)
    """
    if app.openapi_schema:
        return app
    openapi_schema = get_openapi(
        title=app.title,
        version=app.version,
        openapi_version=app.openapi_version,
        summary=app.summary,
        description=app.description,
        terms_of_service=app.terms_of_service,
        contact=app.contact,
        license_info=app.license_info,
        routes=app.routes,
        webhooks=app.webhooks.routes,
        tags=app.openapi_tags,
        servers=app.servers,
        separate_input_output_schemas=app.separate_input_output_schemas,
    )

    # look for the error 422 and change it to 400
    for path in openapi_schema["paths"]:
        for method in openapi_schema["paths"][path]:
            response_422 = openapi_schema["paths"][path][method]["responses"].pop(
                "422", None
            )
            if response_422:
                openapi_schema["paths"][path][method]["responses"]["400"] = response_422

    app.openapi_schema = openapi_schema
    return app


app = FastAPI(
    lifespan=lifespan,
)


app.include_router(routers)

app.add_exception_handler(RequestValidationError, validation_exception_handler)

app = custom_openapi(app=app)
