from marshmallow import Schema, fields
from sqlalchemy import Column, String, Double, Boolean, ForeignKey, Integer, SmallInteger
from sqlalchemy.orm import relationship

from .entity import Entity, Base


class FoodItem(Entity, Base):
    __tablename__ = 'food_items'

    name = Column(String, unique=True, nullable=False)
    is_full_meal = Column(Boolean, nullable=False)
    spoils = Column(Boolean, nullable=False)
    computed_nutrition = Column(Boolean, nullable=False)  # Indicates nutrition to be computed from recipe ingredients
    price = Column(Double)
    price_amount = Column(Double)
    nutrition_amount = Column(Double)
    kcal = Column(Double)
    carbs = Column(Double)
    protein = Column(Double)
    fat = Column(Double)
    fibre = Column(Double)
    dark_leafy_greens_serving_amount = Column(Double)
    other_vegetables_serving_amount = Column(Double)
    fruit_serving_amount = Column(Double)
    grains_starches_serving_amount = Column(Double)
    nuts_seeds_serving_amount = Column(Double)
    legumes_serving_amount = Column(Double)
    dairy_serving_amount = Column(Double)
    season = Column(SmallInteger)
    minimum_pantry_amount = Column(Double)

    price_unit_id = Column(Integer, ForeignKey('units.id'))
    nutrition_unit_id = Column(Integer, ForeignKey('units.id'))
    minimum_pantry_amount_unit_id = Column(Integer, ForeignKey('units.id'))

    price_unit = relationship('Unit', primaryjoin='FoodItem.price_unit_id==Unit.id')
    nutrition_unit = relationship('Unit', primaryjoin='FoodItem.nutrition_unit_id==Unit.id')
    minimum_pantry_amount_unit = relationship('Unit',
                                              primaryjoin='FoodItem.minimum_pantry_amount_unit_id==Unit.id')
    recipe = relationship('Recipe', back_populates='food_item', uselist=False)

    def __init__(self, name, is_full_meal, spoils, computed_nutrition, price=None, price_amount=None,
                 nutrition_amount=None, kcal=None, carbs=None, protein=None, fat=None, fibre=None,
                 dark_leafy_greens_serving_amount=None, other_vegetables_serving_amount=None, fruit_serving_amount=None,
                 grains_starches_serving_amount=None, nuts_seeds_serving_amount=None, legumes_serving_amount=None,
                 dairy_serving_amount=None, season=None, minimum_pantry_amount=None, price_unit_id=None,
                 nutrition_unit_id=None, minimum_pantry_amount_unit_id=None):
        Entity.__init__(self)
        self.name = name
        self.is_full_meal = is_full_meal
        self.spoils = spoils
        self.computed_nutrition = computed_nutrition
        self.price = price
        self.price_amount = price_amount
        self.nutrition_amount = nutrition_amount
        self.kcal = kcal
        self.carbs = carbs
        self.protein = protein
        self.fat = fat
        self.fibre = fibre
        self.dark_leafy_greens_serving_amount = dark_leafy_greens_serving_amount
        self.other_vegetables_serving_amount = other_vegetables_serving_amount
        self.fruit_serving_amount = fruit_serving_amount
        self.grains_starches_serving_amount = grains_starches_serving_amount
        self.nuts_seeds_serving_amount = nuts_seeds_serving_amount
        self.legumes_serving_amount = legumes_serving_amount
        self.dairy_serving_amount = dairy_serving_amount
        self.season = season
        self.minimum_pantry_amount = minimum_pantry_amount
        self.price_unit_id = price_unit_id
        self.nutrition_unit_id = nutrition_unit_id
        self.minimum_pantry_amount_unit_id = minimum_pantry_amount_unit_id


class FoodItemSchema(Schema):
    id = fields.Integer(dump_only=True)
    name = fields.Str()
    is_full_meal = fields.Boolean()
    spoils = fields.Boolean()
    computed_nutrition = fields.Boolean()
    price = fields.Number(required=False)
    price_amount = fields.Number(required=False)
    nutrition_amount = fields.Number(required=False)
    kcal = fields.Number(required=False)
    carbs = fields.Number(required=False)
    protein = fields.Number(required=False)
    fat = fields.Number(required=False)
    fibre = fields.Number(required=False)
    dark_leafy_greens_serving_amount = fields.Number(required=False)
    other_vegetables_serving_amount = fields.Number(required=False)
    fruit_serving_amount = fields.Number(required=False)
    grains_starches_serving_amount = fields.Number(required=False)
    nuts_seeds_serving_amount = fields.Number(required=False)
    legumes_serving_amount = fields.Number(required=False)
    dairy_serving_amount = fields.Number(required=False)
    season = fields.Integer(required=False)
    minimum_pantry_amount = fields.Number(required=False)
    price_unit = fields.Nested('UnitSchema', only=('name', 'name_plural'))
    nutrition_unit = fields.Nested('UnitSchema', only=('name', 'name_plural'))
    minimum_pantry_amount_unit = fields.Nested('UnitSchema', only=('name', 'name_plural'))
    recipe = fields.Nested('RecipeSchema', exclude=('food_item',))
    price_unit_id = fields.Integer(load_only=True, required=False)
    nutrition_unit_id = fields.Integer(load_only=True, required=False)
    minimum_pantry_amount_unit_id = fields.Integer(load_only=True, required=False)

