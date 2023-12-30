from marshmallow import Schema, fields
from sqlalchemy import Column, Integer, ForeignKey, UniqueConstraint, Index, Double, CheckConstraint
from sqlalchemy.orm import relationship

from .entity import Entity, Base


class UnitConversion(Entity, Base):
    __tablename__ = 'unit_conversions'

    unit1_id = Column(Integer, ForeignKey('units.id', ondelete="CASCADE"), nullable=False)
    unit2_id = Column(Integer, ForeignKey('units.id', ondelete="CASCADE"), nullable=False)
    food_item_id = Column(Integer, ForeignKey('food_items.id', ondelete="CASCADE"), nullable=False)
    multiplier = Column(Double, nullable=False)

    unit1 = relationship('Unit', primaryjoin='Unit.id==UnitConversion.unit1_id')
    unit2 = relationship('Unit', primaryjoin='Unit.id==UnitConversion.unit2_id')
    food_item = relationship('FoodItem', back_populates='unit_conversions')

    __table_args__ = (
        UniqueConstraint('unit1_id', 'unit2_id', 'food_item_id', name='unique_food_item_units'),
        Index('ix_unit1_unit2_food_item_id', 'unit1_id', 'unit2_id', 'food_item_id'),
        CheckConstraint('unit1_id < unit2_id', name='unit1_id_lt_unit2_id')
    )

    def __init__(self, unit1_id, unit2_id, food_item_id, multiplier):
        Entity.__init__(self)
        self.unit1_id = unit1_id
        self.unit2_id = unit2_id
        self.food_item_id = food_item_id
        self.multiplier = multiplier


class UnitConversionSchema(Schema):
    unit1 = fields.Nested('Unit')
    unit2 = fields.Nested('Unit')
    food_item = fields.Nested('FoodItem', only=('id', 'name'))
    multiplier = fields.Number()
    unit1_id = fields.Integer(load_only=True)
    unit2_id = fields.Integer(load_only=True)
    food_item_id = fields.Integer(load_only=True)
