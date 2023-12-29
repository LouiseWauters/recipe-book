from flask import Flask, jsonify

from .entities.entity import Base, engine, Session
from .entities.meal_time_category import MealTimeCategory, MealTimeCategorySchema
from .entities.recipe_origin import RecipeOrigin, RecipeOriginSchema
from .entities.recipe_status import RecipeStatus, RecipeStatusSchema
from .entities.unit import Unit, UnitSchema

app = Flask(__name__)

# generate database schema
Base.metadata.create_all(engine)


@app.route("/meal-time-categories")
def get_meal_time_categories():
    session = Session()
    meal_time_categories_db = session.query(MealTimeCategory).all()
    meal_time_categories = MealTimeCategorySchema(many=True).dump(meal_time_categories_db)
    return jsonify(meal_time_categories), 200


@app.route("/recipe-origins")
def get_recipe_origins():
    session = Session()
    recipe_origins_db = session.query(RecipeOrigin).all()
    recipe_origins = RecipeOriginSchema(many=True).dump(recipe_origins_db)
    return jsonify(recipe_origins), 200


@app.route("/recipe-status")
def get_recipe_status():
    session = Session()
    recipe_status_db = session.query(RecipeStatus).all()
    recipe_status = RecipeStatusSchema(many=True).dump(recipe_status_db)
    return jsonify(recipe_status), 200


@app.route("/units")
def get_units():
    session = Session()
    units_db = session.query(Unit).all()
    units = UnitSchema(many=True).dump(units_db)
    return jsonify(units), 200
