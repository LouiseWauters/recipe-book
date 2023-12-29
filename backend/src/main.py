from flask import Flask

from .entities.entity import Base, engine, Session
from .entities.meal_time_category import MealTimeCategory

app = Flask(__name__)

# generate database schema
Base.metadata.create_all(engine)


@app.route("/")
def get_meal_time_categories():
    session = Session()
    meal_time_categories = session.query(MealTimeCategory).all()
    return ",".join([x.name for x in meal_time_categories])
