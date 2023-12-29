from flask import Flask

from .entities.entity import Base, engine, Session
from .entities.meal_time_category import MealTimeCategory
from .entities.recipe_origin import RecipeOrigin
from .entities.recipe_status import RecipeStatus
from .entities.unit import Unit

app = Flask(__name__)

# generate database schema
Base.metadata.create_all(engine)


@app.route("/meal-time-categories")
def get_meal_time_categories():
    session = Session()
    meal_time_categories = session.query(MealTimeCategory).all()
    return ",".join([x.name for x in meal_time_categories])


@app.route("/recipe-origins")
def get_recipe_origins():
    session = Session()
    recipe_origins = session.query(RecipeOrigin).all()
    return ",".join([x.name for x in recipe_origins])


@app.route("/recipe-status")
def get_recipe_status():
    session = Session()
    recipe_status = session.query(RecipeStatus).all()
    return ",".join([x.name for x in recipe_status])


@app.route("/units")
def get_units():
    session = Session()
    units = session.query(Unit).all()
    return ",".join([x.name for x in units])
