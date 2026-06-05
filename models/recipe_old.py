from database.connection import get_recipes_collection, get_favorites_collection
from bson import ObjectId

def init_sample_recipes():
    """Initialize with comprehensive sample recipes if they don't exist"""
    recipes_collection = get_recipes_collection()
    
    sample_recipes = [
        {
            "name": "Jeera Rice",
            "ingredients": ["Rice", "Cumin Seeds (Jeera)", "Oil", "Ghee", "Salt", "Bay Leaf"],
            "steps": "1. Wash and soak rice for 20 mins.\n2. Heat ghee/oil in a pot, add cumin seeds and bay leaf.\n3. Add rice and sauté for a minute.\n4. Add water and salt. Cook until rice is tender and water is absorbed.",
            "image_url": "https://images.unsplash.com/photo-1626082927389-6cd097cdc6ec?w=400",
            "category": "Veg",
            "cooking_time": "25 mins",
            "calories": 210,
            "difficulty": "Easy"
        },
        # ... existing code ...
        {
            "name": "Khichdi",
            "ingredients": ["Rice", "Moong Dal", "Turmeric Powder", "Salt", "Oil", "Ghee", "Cumin Seeds", "Water"],
            "steps": "1. Wash rice and dal together.\n2. Pressure cook with turmeric, salt, and 3 cups of water.\n3. Heat ghee, add cumin seeds for tempering.\n4. Mix the tempering with cooked khichdi and serve hot.",
            "image_url": "https://images.unsplash.com/photo-1631452180519-c014fe946bc7?w=400",
            "category": "Veg",
            "cooking_time": "20 mins",
            "calories": 250,
            "difficulty": "Easy"
        }
    ]
    
    for recipe in sample_recipes:
        # Check if recipe already exists by name to avoid duplicates
        if recipes_collection.count_documents({"name": recipe["name"]}) == 0:
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


