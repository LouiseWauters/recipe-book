from marshmallow import Schema, fields
from sqlalchemy import Column, String

from .entity import Entity, Base


class RecipeStatus(Entity, Base):
    __tablename__ = 'recipe_status'

    name = Column(String, unique=True, nullable=False)

    def __init__(self, name):
        Entity.__init__(self)
        self.name = name


class RecipeStatusSchema(Schema):
    id = fields.Integer(dump_only=True)
    name = fields.Str()
