from flask import Flask, jsonify

from .entities.entity import Base, engine
from .entities.food_item import FoodItem, FoodItemSchema
from .entities.meal import Meal, MealSchema
from .entities.meal_time_category import MealTimeCategory, MealTimeCategorySchema
from .entities.recipe import Recipe, RecipeSchema
from .entities.recipe_origin import RecipeOrigin, RecipeOriginSchema
from .entities.recipe_status import RecipeStatus, RecipeStatusSchema
from .entities.unit import Unit, UnitSchema
from .utils.crud_utils import get_items
from .utils.mock_data import mock_data

app = Flask(__name__)

# generate database schema
Base.metadata.create_all(engine)


@app.route("/meal-time-categories")
def get_meal_time_categories():
    return jsonify(get_items(MealTimeCategory, MealTimeCategorySchema)), 200


@app.route("/recipe-origins")
def get_recipe_origins():
    return jsonify(get_items(RecipeOrigin, RecipeOriginSchema)), 200


@app.route("/recipe-status")
def get_recipe_status():
    return jsonify(get_items(RecipeStatus, RecipeStatusSchema)), 200


@app.route("/units")
def get_units():
    return jsonify(get_items(Unit, UnitSchema)), 200


@app.route("/recipes")
def get_recipes():
    return jsonify(get_items(Recipe, RecipeSchema)), 200


@app.route("/food-items")
def get_food_items():
    mock_data()
    return jsonify(get_items(FoodItem, FoodItemSchema)), 200


@app.route("/meals")
def get_meals():
    return jsonify(get_items(Meal, MealSchema)), 200
