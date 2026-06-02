from database.connection import get_recipes_collection, get_favorites_collection
from bson import ObjectId

def create_recipe(name, ingredients, steps, image_url, category, cooking_time, calories, difficulty, user_id):
    """Create a new recipe"""
    recipes_collection = get_recipes_collection()
    
    if isinstance(ingredients, str):
        ingredients = [i.strip() for i in ingredients.split(',')]
    
    recipe = {
        "name": name,
        "ingredients": ingredients,
        "steps": steps,
        "image_url": image_url,
        "category": category,
        "cooking_time": cooking_time,
        "calories": calories,
        "difficulty": difficulty,
        "user_id": user_id,
        "rating": 0,
        "numRatings": 0
    }
    result = recipes_collection.insert_one(recipe)
    return result.inserted_id

def get_all_recipes():
    """Get all recipes"""
    recipes_collection = get_recipes_collection()
    try:
        recipes = list(recipes_collection.find())
        for recipe in recipes:
            recipe["_id"] = str(recipe["_id"])
        return recipes
    except:
        return []

def get_recipe_by_id(recipe_id):
    """Get recipe by ID"""
    recipes_collection = get_recipes_collection()
    try:
        recipe = recipes_collection.find_one({"_id": ObjectId(recipe_id)})
        if recipe:
            recipe["_id"] = str(recipe["_id"])
        return recipe
    except:
        return None

def get_recipes_by_ingredients(selected_ingredients):
    """Get recipes that contain any of the selected ingredients"""
    if not selected_ingredients:
        return []
    
    recipes_collection = get_recipes_collection()
    try:
        query = {"ingredients": {"$in": selected_ingredients}}
        recipes = list(recipes_collection.find(query))
        for recipe in recipes:
            recipe["_id"] = str(recipe["_id"])
        return recipes
    except:
        return []

def search_recipes(query_text):
    """Search recipes by name or ingredients"""
    recipes_collection = get_recipes_collection()
    try:
        query = {"$or": [
            {"name": {"$regex": query_text, "$options": "i"}},
            {"ingredients": {"$regex": query_text, "$options": "i"}}
        ]}
        recipes = list(recipes_collection.find(query))
        for recipe in recipes:
            recipe["_id"] = str(recipe["_id"])
        return recipes
    except:
        return []

def get_recipes_by_category(category):
    """Get recipes by category"""
    recipes_collection = get_recipes_collection()
    try:
        recipes = list(recipes_collection.find({"category": category}))
        for recipe in recipes:
            recipe["_id"] = str(recipe["_id"])
        return recipes
    except:
        return []

def add_to_favorites(user_id, recipe_id):
    """Add recipe to favorites"""
    favorites_collection = get_favorites_collection()
    try:
        favorite = {"user_id": user_id, "recipe_id": recipe_id}
        existing = favorites_collection.find_one(favorite)
        if not existing:
            favorites_collection.insert_one(favorite)
            return True
    except:
        pass
    return False

def remove_from_favorites(user_id, recipe_id):
    """Remove recipe from favorites"""
    favorites_collection = get_favorites_collection()
    try:
        favorites_collection.delete_one({"user_id": user_id, "recipe_id": recipe_id})
    except:
        pass

def get_favorites(user_id):
    """Get user favorites"""
    favorites_collection = get_favorites_collection()
    recipes_collection = get_recipes_collection()
    try:
        favs = list(favorites_collection.find({"user_id": user_id}))
        recipe_ids = [fav["recipe_id"] for fav in favs]
        recipes = []
        for rid in recipe_ids:
            recipe = recipes_collection.find_one({"_id": ObjectId(rid)})
            if recipe:
                recipe["_id"] = str(recipe["_id"])
                recipes.append(recipe)
        return recipes
    except:
        return []
