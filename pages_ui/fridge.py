import streamlit as st
from models.recipe import get_recipes_by_ingredients

COMMON_INGREDIENTS = [
    "Beans", "Bread", "Burger Buns", "Butter", "Cabbage", "Capsicum", "Carrot", 
    "Cauliflower", "Chicken", "Chilli Sauce", "Coffee Powder", "Coriander Leaves", 
    "Coriander Powder", "Corn Flour", "Cream (Malai)", "Cucumber", "Cumin Seeds (Jeera)", 
    "Egg", "Garam Masala", "Garlic", "Ghee", "Ginger", "Green Chutney", "Green Chilli", 
    "Kitchen King Masala", "Maida", "Mayonnaise", "Milk", "Moong Dal", "Oil", "Onion", 
    "Paneer", "Paratha", "Peas", "Potato", "Red Chilli Powder", "Rice", "Roti", "Salt", 
    "Soy Sauce", "Sugar", "Tomato", "Tomato Ketchup", "Toor Dal", "Turmeric Powder", 
    "Vinegar", "Water", "Wheat Flour (Atta)"
]

def fridge_page():
    """What's in My Fridge page"""
    st.markdown("<h1> What's in My Fridge?</h1>", unsafe_allow_html=True)
    st.markdown("Select the ingredients you have, and we'll find matching recipes!")
    
    # Search bar
    search = st.text_input(" Search ingredients...", placeholder="Search...")
    
    # Filter ingredients
    if search:
        filtered = [i for i in COMMON_INGREDIENTS if search.lower() in i.lower()]
    else:
        filtered = COMMON_INGREDIENTS
    
    # Show ingredient checkboxes in columns
    st.markdown("###  Select Ingredients:")
    cols = st.columns(4)
    selected = []
    
    for i, ingredient in enumerate(filtered):
        with cols[i % 4]:
            if st.checkbox(ingredient, key=f"ing_{ingredient}"):
                selected.append(ingredient)
    
    # Find recipes button
    if st.button(" Find Recipes", type="primary"):
        if selected:
            recipes = get_recipes_by_ingredients(selected)
            if recipes:
                from pages_ui.catalog import display_recipe_cards
                st.markdown(f"###  Found {len(recipes)} Matching Recipes:")
                display_recipe_cards(recipes)
            else:
                st.warning("No recipes found with selected ingredients!")
        else:
            st.warning("Please select at least one ingredient!")
