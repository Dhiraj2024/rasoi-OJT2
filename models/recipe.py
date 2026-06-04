from database.connection import get_recipes_collection, get_favorites_collection
from bson import ObjectId

def init_sample_recipes():
    """Initialize with sample recipes if empty"""
    recipes = get_all_recipes()
    if len(recipes) == 0:
        sample_recipes = [
            {
                "name": "Classic Masala Dosa",
                "ingredients": ["Rice", "Flour", "Potato", "Onion", "Cumin", "Turmeric"],
                "steps": "1. Soak rice overnight\n2. Make batter\n3. Prepare aloo filling\n4. Spread batter on tawa\n5. Add filling and fold",
                "image_url": "https://images.unsplash.com/photo-1668236543090-82eba7ee2b1d?w=400",
                "category": "Veg",
                "cooking_time": "45 mins",
                "calories": 350,
                "difficulty": "Medium"
            },
            {
                "name": "Chicken Butter Masala",
                "ingredients": ["Chicken", "Tomato", "Onion", "Garlic", "Ginger", "Cream", "Butter"],
                "steps": "1. Marinate chicken\n2. Cook onions and spices\n3. Add tomato puree\n4. Add chicken\n5. Finish with cream",
                "image_url": "https://images.unsplash.com/photo-1603894584373-5ac82b2ae398?w=400",
                "category": "Non-Veg",
                "cooking_time": "50 mins",
                "calories": 520,
                "difficulty": "Medium"
            },
            {
                "name": "Palak Paneer",
                "ingredients": ["Paneer", "Spinach", "Onion", "Garlic", "Ginger", "Cream"],
                "steps": "1. Blanch spinach\n2. Make onion paste\n3. Cook spinach with spices\n4. Add paneer cubes\n5. Finish with cream",
                "image_url": "https://images.unsplash.com/photo-1601050690597-df0568f70950?w=400",
                "category": "Veg",
                "cooking_time": "30 mins",
                "calories": 380,
                "difficulty": "Easy"
            },
            {
                "name": "Vegetable Fried Rice",
                "ingredients": ["Rice", "Eggs", "Carrot", "Capsicum", "Onion", "Garlic"],
                "steps": "1. Cook rice and let cool\n2. Scramble eggs\n3. Stir fry vegetables\n4. Add rice and sauce\n5. Mix well",
                "image_url": "https://images.unsplash.com/photo-1512058564366-18510be2db19?w=400",
                "category": "Quick Meals",
                "cooking_time": "20 mins",
                "calories": 320,
                "difficulty": "Easy"
            },
            {
                "name": "Biryani",
                "ingredients": ["Rice", "Chicken", "Onion", "Yogurt", "Ginger", "Garlic"],
                "steps": "1. Marinate chicken\n2. Fry onions\n3. Layer rice and chicken\n4. Cook on high heat\n5. Rest for 5 mins",
                "image_url": "https://images.unsplash.com/photo-1584584867869-25be60d4c81e?w=400",
                "category": "Non-Veg",
                "cooking_time": "60 mins",
                "calories": 580,
                "difficulty": "Hard"
            }
        ]
        for recipe in sample_recipes:
            create_recipe(**recipe, user_id="demo")

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
