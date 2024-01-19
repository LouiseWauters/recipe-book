from ..entities.food_item import FoodItem, FoodItemSchema
from ..entities.recipe import Recipe, RecipeSchema
from ..utils.crud_utils import add_item


def mock_data():
    new_food_item1 = {
        "name": "mihoen",
        "is_full_meal": False,
        "spoils": False,
        "computed_nutrition": False,
        "price": 1.49,
        "price_amount": 250,
        "nutrition_amount": 100,
        "kcal": 329,
        "carbs": 73,
        "protein": 6.4,
        "fat": 0.8,
        "fibre": 2.2,
        "dark_leafy_greens_serving_amount": -1,
        "other_vegetables_serving_amount": -1,
        "fruit_serving_amount": -1,
        "grains_starches_serving_amount": 50,
        "nuts_seeds_serving_amount": -1,
        "legumes_serving_amount": -1,
        "dairy_serving_amount": -1,
        "season": 4095,
        "minimum_pantry_amount": 125,
        "price_unit_id": 1,
        "nutrition_unit_id": 1,
        "minimum_pantry_amount_unit_id": 1
    }
    new_food_item2 = {
        "name": "broccoli",
        "is_full_meal": False,
        "spoils": True,
        "computed_nutrition": False,
        "price": 1.19,
        "price_amount": 500,
        "nutrition_amount": 100,
        "kcal": 33,
        "carbs": 7,
        "protein": 2.8,
        "fat": 0.4,
        "fibre": 1.7,
        "dark_leafy_greens_serving_amount": -1,
        "other_vegetables_serving_amount": 80,
        "fruit_serving_amount": -1,
        "grains_starches_serving_amount": -1,
        "nuts_seeds_serving_amount": -1,
        "legumes_serving_amount": -1,
        "dairy_serving_amount": -1,
        "season": 2032,
        "minimum_pantry_amount": 0,
        "price_unit_id": 1,
        "nutrition_unit_id": 1,
        "minimum_pantry_amount_unit_id": 1
    }
    new_food_item3 = {
        "name": "mihoen met broccoli",
        "is_full_meal": True,
        "spoils": True,
        "computed_nutrition": True,
        "minimum_pantry_amount": 0,
        "minimum_pantry_amount_unit_id": 1
    }
    # quark
    new_food_item4 = {
        "name": "magere kwark",
        "is_full_meal": False,
        "spoils": True,
        "computed_nutrition": False,
        "snooze_days": 14,
        "price": 1.39,
        "price_amount": 500,
        "nutrition_amount": 100,
        "kcal": 52,
        "carbs": 4,
        "protein": 9,
        "fat": 0,
        "fibre": 0,
        "dark_leafy_greens_serving_amount": -1,
        "other_vegetables_serving_amount": -1,
        "fruit_serving_amount": -1,
        "grains_starches_serving_amount": -1,
        "nuts_seeds_serving_amount": -1,
        "legumes_serving_amount": -1,
        "dairy_serving_amount": 200,
        "season": 4095,
        "minimum_pantry_amount": 0,
        "price_unit_id": 1,
        "nutrition_unit_id": 1,
        "minimum_pantry_amount_unit_id": 1
    }
    # cruesli
    item1 = add_item(new_food_item1, FoodItem, FoodItemSchema)
    item2 = add_item(new_food_item2, FoodItem, FoodItemSchema)
    item3 = add_item(new_food_item3, FoodItem, FoodItemSchema)
    new_recipe = {
        "cook_time": 30,
        "prep_time": 20,
        "description": "Een heel povere mihoen.",
        "food_item_id": item3["id"],
        "recipe_status_id": 1,
        "cook_or_origin_id": 2
    }
    add_item(new_recipe, Recipe, RecipeSchema)
