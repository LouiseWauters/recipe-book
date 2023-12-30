from marshmallow import Schema, fields
from sqlalchemy import Column, Date, ForeignKey, Integer, Boolean, Double
from sqlalchemy.orm import relationship

from .entity import Entity, Base


class Meal(Entity, Base):
    __tablename__ = 'meals'

    date = Column(Date, nullable=False)
    plan = Column(Boolean, nullable=False)
    leftovers = Column(Boolean, nullable=False)
    portion_amount = Column(Double)

    portion_amount_unit_id = Column(Integer, ForeignKey('units.id'))
    food_item_id = Column(Integer, ForeignKey('food_items.id', ondelete="CASCADE"), nullable=False)
    meal_time_category_id = Column(Integer, ForeignKey('meal_time_categories.id'), nullable=False)

    portion_amount_unit = relationship('Unit')
    food_item = relationship('FoodItem')
    meal_time_category = relationship('MealTimeCategory')

    def __init__(self, date, plan, leftovers, food_item_id, meal_time_category_id, portion_amount=None,
                 portion_amount_unit_id=None):
        Entity.__init__(self)
        self.date = date
        self.plan = plan
        self.leftovers = leftovers
        self.food_item_id = food_item_id
        self.meal_time_category_id = meal_time_category_id
        self.portion_amount = portion_amount
        self.portion_amount_unit_id = portion_amount_unit_id


class MealSchema(Schema):
    id = fields.Integer(dump_only=True)
    date = fields.Date()
    plan = fields.Boolean()
    leftovers = fields.Boolean()
    portion_amount = fields.Number(required=False)
    portion_amount_unit = fields.Nested('UnitSchema', only=('name', 'name_plural'), required=False)
    food_item = fields.Nested('FoodItemSchema', only=('id', 'name'))
    meal_time_category = fields.Pluck('MealTimeCategorySchema', 'name')
    portion_amount_unit_id = fields.Integer(load_only=True, required=False)
    food_item_id = fields.Integer(load_only=True, required=False)
    meal_time_category_id = fields.Integer(load_only=True, required=False)
