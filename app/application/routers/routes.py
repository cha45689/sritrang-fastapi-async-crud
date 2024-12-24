"""
this file is use to prebundle the route before attach to main app
"""

from fastapi import APIRouter

from app.application.routers.items import item_routes

routers = APIRouter(prefix="/api/v1")

routers.include_router(item_routes)
