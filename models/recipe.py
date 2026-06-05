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
        {
            "name": "Plain Rice",
            "ingredients": ["Rice", "Water", "Salt"],
            "steps": "1. Rinse rice thoroughly.\n2. Boil water in a large pot.\n3. Add rice and salt.\n4. Cook until soft, drain excess water.",
            "image_url": "https://images.unsplash.com/photo-1516684732162-798a0062be99?w=400",
            "category": "Veg",
            "cooking_time": "20 mins",
            "calories": 130,
            "difficulty": "Easy"
        },
        {
            "name": "Roti",
            "ingredients": ["Wheat Flour (Atta)", "Water", "Salt"],
            "steps": "1. Mix flour, salt and water to make a soft dough.\n2. Rest dough for 15 mins.\n3. Roll into thin circles.\n4. Cook on a hot tawa until both sides are puffed and brown.",
            "image_url": "https://images.unsplash.com/photo-1626777553732-48993abc13bc?w=400",
            "category": "Veg",
            "cooking_time": "15 mins",
            "calories": 70,
            "difficulty": "Medium"
        },
        {
            "name": "Kadai Paneer",
            "ingredients": ["Paneer", "Onion", "Tomato", "Capsicum", "Ginger", "Garlic", "Green Chilli", "Oil", "Butter", "Salt", "Turmeric Powder", "Red Chilli Powder", "Coriander Powder", "Garam Masala", "Kitchen King Masala"],
            "steps": "1. Sauté onions, ginger, and garlic.\n2. Add tomato puree and spices, cook until oil separates.\n3. Toss in capsicum and onion petals.\n4. Add paneer cubes and cook for 5 mins.",
            "image_url": "https://images.unsplash.com/photo-1601050690597-df0568f70950?w=400",
            "category": "Veg",
            "cooking_time": "35 mins",
            "calories": 320,
            "difficulty": "Medium"
        },
        {
            "name": "Malai Kofta",
            "ingredients": ["Paneer", "Potato", "Cream (Malai)", "Corn Flour", "Onion", "Tomato", "Ginger", "Garlic", "Oil", "Salt", "Turmeric Powder", "Red Chilli Powder", "Garam Masala"],
            "steps": "1. Mash potato and paneer, add corn flour, make balls (koftas) and deep fry.\n2. Prepare gravy with onion, tomato, ginger, garlic, and spices.\n3. Add cream to the gravy.\n4. Add koftas just before serving.",
            "image_url": "https://images.unsplash.com/photo-1585932231552-05b7a03366bc?w=400",
            "category": "Veg",
            "cooking_time": "50 mins",
            "calories": 450,
            "difficulty": "Hard"
        },
        {
            "name": "Chicken Curry",
            "ingredients": ["Chicken", "Onion", "Tomato", "Ginger", "Garlic", "Oil", "Salt", "Turmeric Powder", "Red Chilli Powder", "Coriander Powder", "Garam Masala", "Chicken Masala"],
            "steps": "1. Sauté onions until golden brown.\n2. Add ginger-garlic paste and tomatoes.\n3. Add chicken and all spices.\n4. Add water and simmer until chicken is cooked through.",
            "image_url": "https://images.unsplash.com/photo-1603894584373-5ac82b2ae398?w=400",
            "category": "Non-Veg",
            "cooking_time": "45 mins",
            "calories": 380,
            "difficulty": "Medium"
        },
        {
            "name": "Egg Curry",
            "ingredients": ["Egg", "Onion", "Tomato", "Ginger", "Garlic", "Oil", "Salt", "Turmeric Powder", "Red Chilli Powder", "Garam Masala"],
            "steps": "1. Boil eggs and peel them.\n2. Sauté onions, ginger, garlic, and tomatoes to make a base.\n3. Add spices and water to make gravy.\n4. Add halved boiled eggs and simmer for 5 mins.",
            "image_url": "https://images.unsplash.com/photo-1542181961-9590d0c79dab?w=400",
            "category": "Non-Veg",
            "cooking_time": "30 mins",
            "calories": 250,
            "difficulty": "Easy"
        },
        {
            "name": "Samosa",
            "ingredients": ["Maida", "Potato", "Peas", "Green Chilli", "Ginger", "Coriander Leaves", "Salt", "Turmeric Powder", "Red Chilli Powder", "Oil"],
            "steps": "1. Make a stiff dough with maida and oil.\n2. Prepare stuffing with boiled potatoes, peas, and spices.\n3. Roll dough, fill with stuffing, and fold into triangles.\n4. Deep fry on low heat until golden.",
            "image_url": "https://images.unsplash.com/photo-1589301760014-d929f3979dbc?w=400",
            "category": "Quick Meals",
            "cooking_time": "60 mins",
            "calories": 300,
            "difficulty": "Hard"
        },
        {
            "name": "Veg Burger",
            "ingredients": ["Burger Buns", "Potato", "Onion", "Tomato", "Cabbage", "Carrot", "Mayonnaise", "Tomato Ketchup", "Salt", "Oil"],
            "steps": "1. Make a patty using mashed potatoes, carrots, and salt; shallow fry.\n2. Toast the burger buns.\n3. Spread mayonnaise and ketchup on buns.\n4. Assemble with patty, onion slices, tomato, and cabbage.",
            "image_url": "https://images.unsplash.com/photo-1550547660-d9450f859349?w=400",
            "category": "Quick Meals",
            "cooking_time": "25 mins",
            "calories": 350,
            "difficulty": "Easy"
        },
        {
            "name": "Veg Sandwich",
            "ingredients": ["Bread", "Potato", "Cucumber", "Tomato", "Butter", "Green Chutney", "Salt"],
            "steps": "1. Butter the bread slices.\n2. Apply green chutney.\n3. Layer with sliced boiled potatoes, cucumber, and tomato.\n4. Sprinkle salt, cover with another slice and grill or serve fresh.",
            "image_url": "https://images.unsplash.com/photo-1528735602780-2552fd46c7af?w=400",
            "category": "Quick Meals",
            "cooking_time": "10 mins",
            "calories": 220,
            "difficulty": "Easy"
        },
        {
            "name": "Veg Roll",
            "ingredients": ["Roti", "Paratha", "Cabbage", "Capsicum", "Carrot", "Onion", "Green Chutney", "Tomato Ketchup", "Salt", "Oil"],
            "steps": "1. Sauté cabbage, capsicum, carrot, and onion with salt.\n2. Take a roti/paratha, spread chutney and ketchup.\n3. Place the sautéed veggies in the center.\n4. Roll it tightly and serve.",
            "image_url": "https://images.unsplash.com/photo-1626700051175-6818013e1d4f?w=400",
            "category": "Quick Meals",
            "cooking_time": "20 mins",
            "calories": 280,
            "difficulty": "Easy"
        },
        {
            "name": "Veg Manchurian",
            "ingredients": ["Cabbage", "Carrot", "Beans", "Maida", "Corn Flour", "Soy Sauce", "Chilli Sauce", "Vinegar", "Garlic", "Ginger", "Green Chilli", "Salt", "Oil"],
            "steps": "1. Mix chopped veggies with maida and corn flour; deep fry balls.\n2. Prepare sauce with ginger, garlic, green chillies, soy sauce, and chilli sauce.\n3. Thicken sauce with corn flour slurry.\n4. Add fried balls to the sauce and toss.",
            "image_url": "https://images.unsplash.com/photo-1637508607685-3f32f75fdc30?w=400",
            "category": "Quick Meals",
            "cooking_time": "40 mins",
            "calories": 310,
            "difficulty": "Medium"
        },
        {
            "name": "Coffee",
            "ingredients": ["Milk", "Coffee Powder", "Sugar", "Water"],
            "steps": "1. Boil water and add coffee powder and sugar.\n2. Add milk and bring to a boil.\n3. Froth it up and serve hot.",
            "image_url": "https://images.unsplash.com/photo-1509042239860-f550ce710b93?w=400",
            "category": "Beverages",
            "cooking_time": "5 mins",
            "calories": 80,
            "difficulty": "Easy"
        },
        {
            "name": "Dal Tadka",
            "ingredients": ["Toor Dal", "Onion", "Tomato", "Garlic", "Ginger", "Oil", "Ghee", "Salt", "Turmeric Powder", "Red Chilli Powder", "Cumin Seeds", "Garam Masala"],
            "steps": "1. Pressure cook dal with salt and turmeric.\n2. Heat ghee, add cumin seeds and garlic.\n3. Sauté onions, ginger, and tomatoes.\n4. Add spices and pour this tadka over the cooked dal.",
            "image_url": "https://images.unsplash.com/photo-1546833999-b9f581a1996d?w=400",
            "category": "Veg",
            "cooking_time": "30 mins",
            "calories": 180,
            "difficulty": "Easy"
        },
        {
            "name": "Aloo Gobi",
            "ingredients": ["Potato", "Cauliflower", "Onion", "Tomato", "Green Chilli", "Oil", "Salt", "Turmeric Powder", "Red Chilli Powder", "Coriander Powder", "Garam Masala"],
            "steps": "1. Sauté cauliflower florets and potato cubes until slightly browned.\n2. Make a base with onions, green chillies, and tomatoes.\n3. Add all spices and the sautéed vegetables.\n4. Cover and cook on low heat until tender.",
            "image_url": "https://images.unsplash.com/photo-1589676762372-fd975bc5158a?w=400",
            "category": "Veg",
            "cooking_time": "25 mins",
            "calories": 200,
            "difficulty": "Easy"
        },
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
    """Get recipes where ALL selected ingredients are present (High Match) 
    or recipes where the majority of ingredients match."""
    if not selected_ingredients:
        return []
    
    recipes_collection = get_recipes_collection()
    try:
        # Find recipes that contain ANY of the selected ingredients
        query = {"ingredients": {"$in": selected_ingredients}}
        recipes = list(recipes_collection.find(query))
        
        # Scoring system: How many selected ingredients match this recipe?
        scored_recipes = []
        for recipe in recipes:
            match_count = len(set(recipe["ingredients"]) & set(selected_ingredients))
            # Only show if at least 50% of the recipe's core ingredients are selected
            # OR at least 2 ingredients match
            if match_count >= 2 or match_count == len(recipe["ingredients"]):
                recipe["_id"] = str(recipe["_id"])
                recipe["match_score"] = match_count
                scored_recipes.append(recipe)
        
        # Sort by best match (highest score)
        scored_recipes.sort(key=lambda x: x["match_score"], reverse=True)
        return scored_recipes
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
