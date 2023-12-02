# main_script.py

import streamlit as st
from themes.homepage import apply_custom_theme
from themes.sidebar import center_sidebar_title


# Set page config
st.set_page_config(
    page_title="Home",
    page_icon="🏠",  # Emoji for the tab icon
    layout="wide",
)

# Apply the custom sidebar theme
apply_custom_theme()

# Add a centered sidebar title
center_sidebar_title("Business Name")


