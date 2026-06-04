import streamlit as st
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Import models and UI components
from models.recipe import init_sample_recipes
from pages_ui.auth import login_page, signup_page
from pages_ui.main_layout import main_app
from pages_ui.catalog import view_recipe_details

# Page configuration
st.set_page_config(
    page_title="Rasoi Guru",
    page_icon="🍳",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
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

    /* Elegant Pill-shaped Buttons */
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

    /* Style Form Inputs & Selection Boxes */
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

    hr {
        border-color: rgba(197, 160, 89, 0.15) !important;
    }
    
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

# Main Execution logic
if __name__ == "__main__":
    # Initialize sample recipes on first run
    try:
        init_sample_recipes()
    except Exception as e:
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
