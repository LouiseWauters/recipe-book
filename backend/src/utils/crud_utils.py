from ..entities.entity import Session


def get_items(item_entity, item_schema):
    session = Session()
    recipe_origins_db = session.query(item_entity).all()
    recipe_origins = item_schema(many=True).dump(recipe_origins_db)
    session.close()
    return recipe_origins


def add_item(item_dict, item_entity, item_schema):
    session = Session()
    new_item = item_schema().load(item_dict)
    item = item_entity(**new_item)
    session.add(item)
    session.commit()
    new_item = item_schema().dump(item)
    session.close()
    return new_item
