import streamlit as st
from models.recipe import remove_from_favorites, get_favorites

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
