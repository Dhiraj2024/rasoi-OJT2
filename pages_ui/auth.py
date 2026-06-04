import streamlit as st
from models.user import get_user_by_email, create_user
from utils.auth import verify_password, hash_password

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
