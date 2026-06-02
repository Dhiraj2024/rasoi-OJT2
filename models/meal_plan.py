from database.connection import get_meal_plans_collection
from bson import ObjectId

def save_meal_plan(user_id, meal_plan):
    """Save or update meal plan"""
    meal_plans_collection = get_meal_plans_collection()
    try:
        existing = meal_plans_collection.find_one({"user_id": user_id})
        if existing:
            meal_plans_collection.update_one(
                {"_id": ObjectId(existing["_id"])},
                {"$set": {"meal_plan": meal_plan}}
            )
        else:
            meal_plans_collection.insert_one({"user_id": user_id, "meal_plan": meal_plan})
    except:
        pass

def get_meal_plan(user_id):
    """Get user meal plan"""
    meal_plans_collection = get_meal_plans_collection()
    try:
        plan = meal_plans_collection.find_one({"user_id": user_id})
        if plan:
            return plan["meal_plan"]
    except:
        pass
    return None
