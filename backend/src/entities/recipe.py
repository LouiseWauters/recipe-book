from marshmallow import Schema, fields
from sqlalchemy import Column, String, Integer, ForeignKey, UniqueConstraint
from sqlalchemy.orm import relationship

from .entity import Entity, Base


class Recipe(Entity, Base):
    __tablename__ = 'recipes'

    original_source_link = Column(String)
    cook_time = Column(Integer)
    prep_time = Column(Integer)
    rest_time = Column(Integer)
    description = Column(String)

    food_item_id = Column(Integer, ForeignKey('food_items.id', ondelete="CASCADE"), nullable=False)
    recipe_status_id = Column(Integer, ForeignKey('recipe_status.id'), nullable=False)
    cook_or_origin_id = Column(Integer, ForeignKey('recipe_origins.id'), nullable=False)

    food_item = relationship('FoodItem', back_populates='recipe')
    recipe_status = relationship('RecipeStatus')
    cook_or_origin = relationship('RecipeOrigin')

    __table_args__ = (UniqueConstraint("food_item_id"),)

    def __init__(self, food_item_id, recipe_status_id, cook_or_origin_id, original_source_link=None, cook_time=None,
                 prep_time=None, rest_time=None, description=None):
        Entity.__init__(self)
        self.food_item_id = food_item_id
        self.recipe_status_id = recipe_status_id
        self.cook_or_origin_id = cook_or_origin_id
        self.original_source_link = original_source_link
        self.cook_time = cook_time
        self.prep_time = prep_time
        self.rest_time = rest_time
        self.description = description


class RecipeSchema(Schema):
    id = fields.Integer(dump_only=True)
    original_source_link = fields.Str(required=False)
    cook_time = fields.Integer(required=False)
    prep_time = fields.Integer(required=False)
    rest_time = fields.Integer(required=False)
    description = fields.Str(required=False)
    food_item = fields.Nested('FoodItemSchema', only=('id', 'name', 'price_amount'))
    recipe_status = fields.Pluck('RecipeStatusSchema', 'name')
    cook_or_origin = fields.Pluck('RecipeOriginSchema', 'name')
    food_item_id = fields.Integer(load_only=True, required=False)
    recipe_status_id = fields.Integer(load_only=True, required=False)
    cook_or_origin_id = fields.Integer(load_only=True, required=False)
