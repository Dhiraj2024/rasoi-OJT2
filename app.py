import streamlit as st
import os
from dotenv import load_dotenv

# Load environment variables Test@123456 john@example.com
load_dotenv()

# Import models and utilities
from models.user import create_user, get_user_by_email, get_user_by_id
from models.recipe import (
    create_recipe, get_all_recipes, get_recipe_by_id, 
    get_recipes_by_ingredients, search_recipes, get_recipes_by_category,
    add_to_favorites, remove_from_favorites, get_favorites
)
from models.meal_plan import save_meal_plan, get_meal_plan
from utils.auth import hash_password, verify_password

# Page configuration
st.set_page_config(
    page_title="Rasoi Guru ",
    page_icon="",
    layout="wide",
    initial_sidebar_state="expanded"
)


st.markdown("""
<style>
    /* Import an elegant Serif font for headings */
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400..900;1,400..900&family=Inter:wght@300;400;500&display=swap');

    :root {
        --primary-gold: #C5A059;
        --bg-dark-teal: #012326;
        --text-warm-white: #EAE3D2;
        --text-muted: #8A9A96;
    }

    /* Overall Main App Theme */
    .stApp {
        background-color: var(--bg-dark-teal) !important;
        color: var(--text-warm-white) !important;
        font-family: 'Inter', sans-serif;
    }

    /* Target headers to use the luxurious Serif font styling */
    h1, h2, h3, h4, h5, h6 {
        font-family: 'Playfair Display', serif !important;
        color: var(--primary-gold) !important;
        font-weight: 300 !important;
        letter-spacing: 0.05em !important;
        text-transform: uppercase;
    }

    /* Main App Banner / Page Header Tweaks */
    h1 {
        font-size: 3rem !important;
        border-bottom: 1px solid rgba(197, 160, 89, 0.2);
        padding-bottom: 10px;
        margin-bottom: 25px !important;
    }

    /* Sidebar Restyling to Match the Moody Aesthetic */
    [data-testid="stSidebar"] {
        background-color: #00181A !important;
        border-right: 1px solid rgba(197, 160, 89, 0.15);
    }
    
    [data-testid="stSidebar"] * {
        color: var(--text-warm-white) !important;
    }

    /* Elegant Pill-shaped Buttons mirroring 'EXPLORE' from reference */
    .stButton > button {
        border-radius: 30px !important;
        border: 1px solid var(--primary-gold) !important;
        background-color: transparent !important;
        color: var(--primary-gold) !important;
        font-family: 'Inter', sans-serif;
        font-size: 14px !important;
        text-transform: uppercase;
        letter-spacing: 0.1em;
        padding: 10px 24px !important;
        transition: all 0.3s ease;
    }
    
    .stButton > button:hover {
        background-color: var(--primary-gold) !important;
        color: var(--bg-dark-teal) !important;
        box-shadow: 0px 4px 15px rgba(197, 160, 89, 0.3);
    }

    /* Streamlit Containers as Sleek Recipe Cards */
    [data-testid="stVerticalBlock"] > div > div > .stContainer {
        background-color: #012B2E !important;
        border: 1px solid rgba(197, 160, 89, 0.1) !important;
        border-radius: 8px !important;
        padding: 24px !important;
        margin-bottom: 20px !important;
        transition: border 0.3s ease;
    }

    [data-testid="stVerticalBlock"] > div > div > .stContainer:hover {
        border: 1px solid rgba(197, 160, 89, 0.4) !important;
    }

    /* Style Form Inputs & Selection Boxes nicely */
    .stTextInput input, .stTextArea textarea, .stSelectbox div[data-baseweb="select"] {
        background-color: #00181A !important;
        color: var(--text-warm-white) !important;
        border: 1px solid rgba(197, 160, 89, 0.2) !important;
        border-radius: 4px;
    }

    .stTextInput input:focus, .stTextArea textarea:focus {
        border-color: var(--primary-gold) !important;
        box-shadow: 0 0 0 1px var(--primary-gold) !important;
    }

    /* Horizontal line dividers */
    hr {
        border-color: rgba(197, 160, 89, 0.15) !important;
    }
    
    /* Utility Text */
    .recipe-meta-text {
        color: var(--text-muted);
        font-size: 14px;
    }
</style>
""", unsafe_allow_html=True)

# Session state initialization
if "user" not in st.session_state:
    st.session_state.user = None
if "page" not in st.session_state:
    st.session_state.page = "Login"

# Common ingredients for fridge
COMMON_INGREDIENTS = [
    "Potato", "Tomato", "Onion", "Garlic", "Ginger", "Paneer", "Chicken",
    "Rice", "Wheat", "Flour", "Eggs", "Milk", "Olive Oil", "Butter",
    "Cumin", "Turmeric", "Chilli", "Salt", "Pepper", "Coriander",
    "Carrot", "Capsicum", "Mushroom", "Spinach", "Lettuce", "Cucumber",
    "Yogurt", "Cream", "Cheese", "Bread", "Pasta", "Sugar"
]

# Recipe categories
RECIPE_CATEGORIES = ["Veg", "Non-Veg", "Quick Meals", "Desserts", "Beverages"]

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

# ============ AUTH PAGES ============

def login_page():
    """Login page"""
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown("<h1 style='text-align: center;'> Rasoi Guru</h1>", unsafe_allow_html=True)
        st.markdown("<p style='text-align: center; font-size: 20px;'>Your Kitchen Companion</p>", unsafe_allow_html=True)
        
        with st.form("login_form"):
            email = st.text_input(" Email", placeholder="your@email.com")
            password = st.text_input(" Password", type="password")
            submit = st.form_submit_button("Login", type="primary")
            
            if submit:
                if not email or not password:
                    st.error("Please fill in all fields")
                else:
                    user = get_user_by_email(email)
                    if user and verify_password(password, user["password"]):
                        st.session_state.user = {"_id": str(user["_id"]), "email": user["email"], "name": user["name"]}
                        st.rerun()
                    else:
                        st.error("Invalid email or password")
        
        st.markdown("---")
        st.markdown("<p style='text-align: center;'>Don't have an account?</p>", unsafe_allow_html=True)
        
        if st.button("Sign Up"):
            st.session_state.page = "Signup"
            st.rerun()

def signup_page():
    """Signup page"""
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown("<h1 style='text-align: center;'> Join Rasoi Guru</h1>", unsafe_allow_html=True)
        
        with st.form("signup_form"):
            name = st.text_input(" Name", placeholder="Your name")
            email = st.text_input(" Email", placeholder="your@email.com")
            password = st.text_input(" Password", type="password", placeholder="Min 6 characters")
            confirm = st.text_input(" Confirm Password", type="password")
            submit = st.form_submit_button("Sign Up", type="primary")
            
            if submit:
                if not all([name, email, password, confirm]):
                    st.error("Please fill in all fields")
                elif len(password) < 6:
                    st.error("Password must be at least 6 characters!")
                elif password != confirm:
                    st.error("Passwords don't match!")
                elif get_user_by_email(email):
                    st.error("Email already registered!")
                else:
                    hashed = hash_password(password)
                    create_user(email, hashed, name)
                    st.success("Account created! Please login.")
                    st.session_state.page = "Login"
                    st.rerun()
        
        st.markdown("---")
        if st.button("Back to Login"):
            st.session_state.page = "Login"
            st.rerun()

# ============ MAIN APP ============

def main_app():
    """Main application"""
    user_id = st.session_state.user["_id"]
    
    # Sidebar
    with st.sidebar:
        st.image("https://cdn.dribbble.com/userupload/43440150/file/original-7acd7ff6bc89b3a092f8418fa5469d9e.jpg?format=webp&resize=400x300&vertical=center", width=80)
        st.markdown("<h2>Rasoi Guru </h2>", unsafe_allow_html=True)
        
        # st.markdown("---")
        # st.markdown(f"###  {st.session_state.user['name']}")
        
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
        meal_planner_page()
    elif menu == " Favorites":
        favorites_page()

# ============ FRIDGE PAGE ============

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
                st.markdown(f"###  Found {len(recipes)} Matching Recipes:")
                display_recipe_cards(recipes)
            else:
                st.warning("No recipes found with selected ingredients!")
        else:
            st.warning("Please select at least one ingredient!")

# ============ CATALOG PAGE ============

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

# ============ ADD RECIPE PAGE ============

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

# ============ MEAL PLANNER PAGE ============

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

# ============ FAVORITES PAGE ============

def favorites_page():
    """Favorites page"""
    st.markdown("<h1> My Favorites</h1>", unsafe_allow_html=True)
    
    user_id = st.session_state.user["_id"]
    favorites = get_favorites(user_id)
    
    if favorites:
        st.markdown(f"### You have {len(favorites)} favorite recipes")
        
        for recipe in favorites:
            with st.container():
                col1, col2 = st.columns([1, 2])
                
                with col1:
                    try:
                        st.image(recipe.get("image_url", "https://img.icons8.com/fluency/100/cooking-pot.png"), width=150)
                    except:
                        st.image("https://img.icons8.com/fluency/100/cooking-pot.png", width=150)
                
                with col2:
                    st.markdown(f"### {recipe['name']}")
                    st.markdown(f"**Category:** {recipe.get('category', 'N/A')}")
                    st.markdown(f"** Time:** {recipe.get('cooking_time', 'N/A')}")
                    
                    col_btn1, col_btn2 = st.columns(2)
                    with col_btn1:
                        if st.button("View Details", key=f"fav_view_{recipe['_id']}"):
                            st.session_state.view_recipe = recipe
                            st.rerun()
                    with col_btn2:
                        if st.button("? Remove", key=f"remove_{recipe['_id']}"):
                            remove_from_favorites(user_id, recipe["_id"])
                            st.success("Removed from favorites!")
                            st.rerun()
                
                st.markdown("---")
    else:
        st.info("You don't have any favorite recipes yet! ")
        if st.button("Browse Recipes"):
            st.rerun()

# ============ MAIN EXECUTION ============

if __name__ == "__main__":
    # Initialize sample recipes on first run
    try:
        init_sample_recipes()
    except:
        pass
    
    # Show appropriate page based on authentication status
    if st.session_state.user:
        # Check if viewing recipe details
        if "view_recipe" in st.session_state and st.session_state.view_recipe:
            view_recipe_details(st.session_state.view_recipe["_id"])
        else:
            main_app()
    else:
        # Show login/signup pages
        if st.session_state.page == "Login":
            login_page()
        elif st.session_state.page == "Signup":
            signup_page()
