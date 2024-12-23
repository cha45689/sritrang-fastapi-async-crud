"""
This module is use to declare Item model and relate model
"""
from tortoise import fields, models
from tortoise.contrib.pydantic import pydantic_model_creator


class ItemsORM(models.Model):
    """
    Base Item model for ORM and later generate pydantic model
    """
    id = fields.IntField(primary_key=True)
    name = fields.CharField(max_length=255)
    description = fields.CharField(max_length=65535)


ItemInput = pydantic_model_creator(ItemsORM, exclude_readonly=True)
Item = pydantic_model_creator(ItemsORM)
