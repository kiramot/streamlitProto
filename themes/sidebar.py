# sidebar_theme.py

import base64
import streamlit as st

@st.cache_data
def get_sidebar_img_as_base64(file):
    with open(file, "rb") as f:
        return base64.b64encode(f.read()).decode()

def apply_sidebar_theme():
    _apply_sidebar_background()

def _apply_sidebar_background():
    svg_bg_file = "images/sd.svg"
    sidebar_img = get_sidebar_img_as_base64(svg_bg_file)

    page_bg_img = f"""
    <style>
    [data-testid="stSidebar"] {{
      background-image: url("data:image/svg+xml;base64,{sidebar_img}");
      background-size: cover;
      background-position: center center;
      background-repeat: no-repeat;
      background-attachment: local;
      flex: 0 0 auto;
    }}
    </style>
    """

    st.markdown(page_bg_img, unsafe_allow_html=True)

def center_sidebar_title(title):
    st.sidebar.markdown("<br>", unsafe_allow_html=True)
    st.sidebar.markdown(f"""
        <div style="text-align: center;">
            <h1>{title}</h1>
        </div>
    """, unsafe_allow_html=True)
