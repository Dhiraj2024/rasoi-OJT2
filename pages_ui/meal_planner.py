import streamlit as st
from models.recipe import get_all_recipes
from models.meal_plan import save_meal_plan, get_meal_plan

def meal_planner_page():
    """Meal Planner page"""
    st.markdown("<h1> Weekly Meal Planner</h1>", unsafe_allow_html=True)
    
    user_id = st.session_state.user["_id"]
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    
    # Get current meal plan
    current_plan = get_meal_plan(user_id) or {}
    
    # Create meal plan form
    meal_plan = {}
    cols = st.columns(4)
    
    for day_idx, day in enumerate(days):
        col = cols[day_idx % 4]
        with col:
            st.subheader(f" {day}")
            recipes = get_all_recipes()
            recipe_names = ["No Recipe"] + [r["name"] for r in recipes]
            
            current_recipe = current_plan.get(day, "No Recipe")
            selected = st.selectbox(f"Select recipe for {day}", recipe_names, 
                                   index=recipe_names.index(current_recipe) if current_recipe in recipe_names else 0,
                                   key=f"day_{day}")
            meal_plan[day] = selected
    
    col1, col2, col3 = st.columns(3)
    with col2:
        if st.button(" Save Meal Plan", type="primary"):
            save_meal_plan(user_id, meal_plan)
            st.success("Meal plan saved! ")
            st.rerun()
