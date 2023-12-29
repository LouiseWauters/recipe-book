from sqlalchemy import Column, String

from .entity import Entity, Base


class RecipeOrigin(Entity, Base):
    __tablename__ = 'recipe_origins'

    name = Column(String, unique=True, nullable=False)

    def __init__(self, name):
        Entity.__init__(self)
        self.name = name
