import streamlit as st
from models.recipe import create_recipe

RECIPE_CATEGORIES = ["Veg", "Non-Veg", "Quick Meals", "Desserts", "Beverages"]

def add_recipe_page():
    """Add Recipe page"""
    st.markdown("<h1>? Add Recipe</h1>", unsafe_allow_html=True)
    st.markdown("Share your delicious recipe with the community!")
    
    with st.form("add_recipe_form"):
        name = st.text_input(" Recipe Name", placeholder="e.g., Butter Chicken")
        
        ingredients = st.text_area(" Ingredients (comma separated)", 
                                  placeholder="e.g., Chicken, Tomato, Onion, Garlic, Ginger, Cream")
        
        steps = st.text_area(" Cooking Steps", placeholder="Step by step instructions...")
        
        col1, col2 = st.columns(2)
        with col1:
            image_url = st.text_input("? Image URL", placeholder="https://...")
        with col2:
            category = st.selectbox("Category", RECIPE_CATEGORIES)
        
        col3, col4 = st.columns(2)
        with col3:
            cooking_time = st.text_input(" Cooking Time", placeholder="e.g., 30 mins")
        with col4:
            difficulty = st.selectbox("Difficulty", ["Easy", "Medium", "Hard"])
        
        col5, col6 = st.columns(2)
        with col5:
            calories = st.number_input(" Calories", min_value=0, step=10)
        with col6:
            pass  # Empty column for alignment
        
        submit = st.form_submit_button("? Add Recipe", type="primary")
        
        if submit:
            if not all([name, ingredients, steps, image_url, cooking_time]):
                st.error("Please fill in all fields!")
            else:
                user_id = st.session_state.user["_id"]
                create_recipe(
                    name=name,
                    ingredients=ingredients,
                    steps=steps,
                    image_url=image_url,
                    category=category,
                    cooking_time=cooking_time,
                    calories=int(calories),
                    difficulty=difficulty,
                    user_id=user_id
                )
                st.success("Recipe added successfully! ")
