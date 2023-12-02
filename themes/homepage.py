# theme.py

import base64
import streamlit as st

@st.cache_data
def get_img_as_base64(file):
    with open(file, "rb") as f:
        return base64.b64encode(f.read()).decode()

def apply_custom_theme():
    # Use an SVG file for the sidebar background
    sidebar_img = get_img_as_base64("images/sd.svg")

    # Use an SVG file for the main background
    main_svg_img = get_img_as_base64("images/homepage.svg")

    # Semi-transparent overlay color
    overlay_color = "rgba(0, 0, 0, 0)"

    page_bg_img = f"""
    <style>
    [data-testid="stAppViewContainer"] {{
      display: flex;
    }}

    [data-testid="stSidebar"] {{
      background-image: url("data:image/svg+xml;base64,{sidebar_img}");
      background-size: cover;
      background-position: center center;
      background-repeat: no-repeat;
      background-attachment: local;
      flex: 0 0 auto;
    }}

    [data-testid="stAppViewContainer"] > .main {{
      flex: 1;
      background-image: url("data:image/svg+xml;base64,{main_svg_img}");
      background-size: cover;
      background-position: top center;
      background-repeat: no-repeat;
      background-attachment: local;
      position: relative;
    }}

    [data-testid="stAppViewContainer"] > .main::before {{
      content: "";
      position: absolute;
      top: 0;
      left: 0;
      width: 100%;
      height: 100%;
      background-color: {overlay_color};
    }}

    [data-testid="stHeader"],
    [data-testid="stToolbar"] {{
      background: rgba(0,0,0,0);
    }}

    [data-testid="stToolbar"] {{
      right: 2rem;
    }}
    </style>
    """

    st.markdown(page_bg_img, unsafe_allow_html=True)
