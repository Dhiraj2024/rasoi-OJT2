import streamlit as st
from pages_ui.fridge import fridge_page
from pages_ui.catalog import catalog_page
from pages_ui.recipe_mgmt import add_recipe_page
from pages_ui.favorites import favorites_page
# Assuming meal_planner_page exists or will be moved
# from pages_ui.meal_planner import meal_planner_page 

def main_app():
    """Main application"""
    user_id = st.session_state.user["_id"]
    
    # Sidebar
    with st.sidebar:
        st.image("https://cdn.dribbble.com/userupload/43440150/file/original-7acd7ff6bc89b3a092f8418fa5469d9e.jpg?format=webp&resize=400x300&vertical=center", width=80)
        st.markdown("<h2>Rasoi Guru </h2>", unsafe_allow_html=True)
        
        # Navigation
        menu = st.radio("Menu", [
            " What's in My Fridge",
            " Recipe Catalog", 
            "? Add Recipe",
            " Meal Planner",
            " Favorites"
        ])     
          
        st.markdown("---")
        
        if st.button(" Logout"):
            st.session_state.user = None
            st.rerun()
    
    # Page routing
    if menu == " What's in My Fridge":
        fridge_page()
    elif menu == " Recipe Catalog":
        catalog_page()
    elif menu == "? Add Recipe":
        add_recipe_page()
    elif menu == " Meal Planner":
        # Temporary placeholder if meal_planner_page is not yet moved
        if 'meal_planner_page' in globals():
            meal_planner_page()
        else:
            from pages_ui.meal_planner import meal_planner_page
            meal_planner_page()
    elif menu == " Favorites":
        favorites_page()
