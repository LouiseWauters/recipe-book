from sqlalchemy import Column, String

from .entity import Entity, Base


class MealTimeCategory(Entity, Base):
    __tablename__ = 'meal_time_categories'

    name = Column(String, unique=True)

    def __init__(self, name):
        Entity.__init__(self)
        self.name = name
