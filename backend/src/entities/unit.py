from marshmallow import Schema, fields
from sqlalchemy import Column, String

from .entity import Entity, Base


class Unit(Entity, Base):
    __tablename__ = 'units'

    name = Column(String, unique=True, nullable=False)
    name_plural = Column(String, nullable=False)

    def __init__(self, name, name_plural):
        Entity.__init__(self)
        self.name = name
        self.name_plural = name_plural


class UnitSchema(Schema):
    id = fields.Integer(dump_only=True)
    name = fields.Str()
    name_plural = fields.Str()
