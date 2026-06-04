import streamlit as st
from models.recipe import (
    get_all_recipes, get_recipe_by_id, search_recipes, 
    get_recipes_by_category, add_to_favorites
)

RECIPE_CATEGORIES = ["Veg", "Non-Veg", "Quick Meals", "Desserts", "Beverages"]

def catalog_page():
    """Recipe Catalog page"""
    st.markdown("<h1> Recipe Catalog</h1>", unsafe_allow_html=True)
    
    # Search bar
    search = st.text_input(" Search recipes...", placeholder="Search recipes...")
    
    # Filter by category
    col1, col2 = st.columns([1, 3])
    with col1:
        category = st.selectbox("Category", ["All"] + RECIPE_CATEGORIES)
    
    # Get recipes
    if search:
        recipes = search_recipes(search)
    elif category != "All":
        recipes = get_recipes_by_category(category)
    else:
        recipes = get_all_recipes()
    
    st.markdown(f"### ? {len(recipes)} Recipes Found")
    
    if recipes:
        display_recipe_cards(recipes)
    else:
        st.info("No recipes found!")

def display_recipe_cards(recipes):
    """Display recipes in card format"""
    for recipe in recipes:
        with st.container():
            col1, col2 = st.columns([1, 2])
            
            with col1:
                try:
                    st.image(recipe.get("image_url", "https://img.icons8.com/fluency/100/cooking-pot.png"), width=200)
                except:
                    st.image("https://img.icons8.com/fluency/100/cooking-pot.png", width=200)
            
            with col2:
                st.markdown(f"### {recipe['name']}")
                st.markdown(f"**Category:** {recipe.get('category', 'N/A')} | **Difficulty:** {recipe.get('difficulty', 'N/A')}")
                st.markdown(f"** Time:** {recipe.get('cooking_time', 'N/A')} | ** Calories:** {recipe.get('calories', 'N/A')}")
                
                col_btn1, col_btn2, col_btn3 = st.columns(3)
                with col_btn1:
                    if st.button("View Details", key=f"view_{recipe['_id']}"):
                        st.session_state.view_recipe = recipe
                        st.rerun()
                with col_btn2:
                    user_id = st.session_state.user["_id"]
                    if st.button(" Favorite", key=f"fav_{recipe['_id']}"):
                        add_to_favorites(user_id, recipe["_id"])
                        st.success("Added to favorites!")
                with col_btn3:
                    if st.button(" Add to Plan", key=f"plan_{recipe['_id']}"):
                        st.session_state.add_to_plan = recipe["_id"]
                        st.rerun()
            
            st.markdown("---")

def view_recipe_details(recipe_id):
    """View recipe details"""
    recipe = get_recipe_by_id(recipe_id)
    if recipe:
        st.markdown(f"# {recipe['name']}")
        
        col1, col2 = st.columns([1, 1])
        with col1:
            try:
                st.image(recipe.get("image_url", "https://img.icons8.com/fluency/100/cooking-pot.png"), width=300)
            except:
                st.image("https://img.icons8.com/fluency/100/cooking-pot.png", width=300)
        
        with col2:
            st.markdown(f"**Category:** {recipe.get('category', 'N/A')}")
            st.markdown(f"**Difficulty:** {recipe.get('difficulty', 'N/A')}")
            st.markdown(f"** Time:** {recipe.get('cooking_time', 'N/A')}")
            st.markdown(f"** Calories:** {recipe.get('calories', 'N/A')}")
            
            user_id = st.session_state.user["_id"]
            if st.button(" Add to Favorites"):
                add_to_favorites(user_id, recipe["_id"])
                st.success("Added to favorites!")
            
            if st.button(" Add to Meal Plan"):
                st.session_state.add_to_plan = recipe["_id"]
                st.rerun()
        
        st.markdown("###  Ingredients:")
        for ing in recipe.get("ingredients", []):
            st.markdown(f"- {ing}")
        
        st.markdown("###  Steps:")
        st.write(recipe.get("steps", "No steps provided"))
        
        if st.button("? Back to Catalog"):
            if "view_recipe" in st.session_state:
                del st.session_state["view_recipe"]
            st.rerun()
