import streamlit as st
from streamlit_gsheets import GSheetsConnection
from streamlit_image_comparison import image_comparison

# Set page configuration
st.set_page_config(
   page_title="Room",
   page_icon="🛏️",  # Emoji for the tab icon
   layout="wide",
)

# Apply custom CSS styles for centering and responsiveness
st.markdown(
   """
   <style>
       body {
           min-height: 100vh;
           margin: 0;
           display: flex;
           flex-direction: column;
           justify-content: center;
           align-items: center;
           background-color: #f4f4f4;  /* Set a background color if needed */
       }
       .css-1l02z4d {
           width: 100% !important;
           max-width: 1000px;  /* Adjust the max-width as needed */
       }
   </style>
   """,
   unsafe_allow_html=True
)

# Apply sidebar theme
from themes.sidebar import apply_sidebar_theme, center_sidebar_title
apply_sidebar_theme()

# Add a centered sidebar title
center_sidebar_title("Business Name")

# Display Title and Description
st.title("Room Availability Portal")
st.markdown("Enter the details of the new vendor below.")

# Establishing a Google Sheets connection
conn = st.connection("gsheets", type=GSheetsConnection)

# Function to create a star rating
def create_star_rating(star_id, rating):
    stars_html = ""
    for i in range(1, 6):
        stars_html += f'<span class="star" data-value="{i}" onclick="{star_id}_clicked({i})">&#9733;</span>'

    return f"""
        <div id="{star_id}" class="rating" style="text-align: center;">
            {stars_html}
        </div>
        <script>
            function {star_id}_clicked(value) {{
                for (let i = 1; i <= 5; i++) {{
                    let star = document.getElementById('{star_id}').querySelector(\`[data-value="\${i}"]\`);
                    if (i <= value) {{
                        star.style.color = 'gold';
                    }} else {{
                        star.style.color = 'gray';
                    }}
                }}
            }}
        </script>
    """

# Define customer IDs and image paths
customer_id_room1 = 1
customer_id_room2 = 2
customer_id_room3 = 3
image_path_room1 = "images/room1.jpg"
image_path_room2 = "images/room2.jpg"
image_path_room3 = "images/room3.jpg"

# Fetch existing vendors data for each room, including Availability and Date of Availability
existing_data_room1 = conn.read(worksheet="room", usecols=["Description", "Price", "Availability", "Date of Availability"], ttl=5).dropna(how="all")
existing_data_room2 = conn.read(worksheet="room", usecols=["Description", "Price", "Availability", "Date of Availability"], ttl=5).dropna(how="all")
existing_data_room3 = conn.read(worksheet="room", usecols=["Description", "Price", "Availability", "Date of Availability"], ttl=5).dropna(how="all")
existing_data_room4 = conn.read(worksheet="room", usecols=["Description", "Price", "Availability", "Date of Availability"], ttl=5).dropna(how="all")
existing_data_room5 = conn.read(worksheet="room", usecols=["Description", "Price", "Availability", "Date of Availability"], ttl=5).dropna(how="all")
existing_data_room6 = conn.read(worksheet="room", usecols=["Description", "Price", "Availability", "Date of Availability"], ttl=5).dropna(how="all")
existing_data_room7 = conn.read(worksheet="room", usecols=["Description", "Price", "Availability", "Date of Availability"], ttl=5).dropna(how="all")

# Tabs
tab1, tab2, tab3, tab4, tab5, tab6, tab7 = st.tabs(["Room1", "Room2", "Room3", "Room4", "Room5", "Room6", "Room7"])

# Tab 1
with tab1:
    st.markdown("<h1 style='text-align: center;'>Room 1</h1>", unsafe_allow_html=True)
    image_comparison(img1=image_path_room1,
                    img2=image_path_room2,
                    label1="Bathroom",
                    label2="Bedroom",
                    width=2000,
                    starting_position=50,
                    show_labels=True,
                    make_responsive=True,
                    in_memory=True,
                    )
    col1, col2 = st.columns(2)
  
    col1.write("<div style='font-size: 18px; text-align: center;'><b>Description:</b> " + str(existing_data_room1["Description"].iloc[0]) + "</div>", unsafe_allow_html=True)
    col2.write("<div style='font-size: 18px; text-align: center;'><b>Price:</b> ₱" + str(existing_data_room1["Price"].iloc[0]) + "</div>", unsafe_allow_html=True)
    col2.write("<div style='font-size: 18px; text-align: center;'><b>Availability:</b> " + str(existing_data_room1["Availability"].iloc[0]) + "</div>", unsafe_allow_html=True)
    col2.write("<div style='font-size: 18px; text-align: center;'><b>Date of Availability:</b> " + str(existing_data_room1["Date of Availability"].iloc[0]) + "</div>", unsafe_allow_html=True)
    col2.write(create_star_rating("star_room1", 0), unsafe_allow_html=True)

# Tab 2
with tab2:
    st.markdown("<h1 style='text-align: center;'>Room 2</h1>", unsafe_allow_html=True)
    st.markdown("<div style='display: flex; justify-content: center;'>", unsafe_allow_html=True)
    st.image("images/room1.jpg", caption='Sunrise by the mountains', width=2000)
    st.markdown("</div>", unsafe_allow_html=True)
    col1, col2 = st.columns(2)
  
    col1.write("<div style='font-size: 18px; text-align: center;'><b>Description:</b> " + str(existing_data_room2["Description"].iloc[0]) + "</div>", unsafe_allow_html=True)
    col2.write("<div style='font-size: 18px; text-align: center;'><b>Price:</b> ₱" + str(existing_data_room2["Price"].iloc[0]) + "</div>", unsafe_allow_html=True)
    col2.write("<div style='font-size: 18px; text-align: center;'><b>Availability:</b> " + str(existing_data_room2["Availability"].iloc[0]) + "</div>", unsafe_allow_html=True)
    col2.write("<div style='font-size: 18px; text-align: center;'><b>Date of Availability:</b> " + str(existing_data_room2["Date of Availability"].iloc[0]) + "</div>", unsafe_allow_html=True)
    col2.write(create_star_rating("star_room2", 0), unsafe_allow_html=True)

# Tab 3
with tab3:
    st.markdown("<h1 style='text-align: center;'>Room 3</h1>", unsafe_allow_html=True)
    st.markdown("<div style='display: flex; justify-content: center;'>", unsafe_allow_html=True)
    st.image("images/room2.jpg", caption='Sunrise by the mountains', width=2000)
    st.markdown("</div>", unsafe_allow_html=True)
    col1, col2 = st.columns(2)
  
    col1.write("<div style='font-size: 18px; text-align: center;'><b>Description:</b> " + str(existing_data_room3["Description"].iloc[0]) + "</div>", unsafe_allow_html=True)
    col2.write("<div style='font-size: 18px; text-align: center;'><b>Price:</b> ₱" + str(existing_data_room3["Price"].iloc[0]) + "</div>", unsafe_allow_html=True)
    col2.write("<div style='font-size: 18px; text-align: center;'><b>Availability:</b> " + str(existing_data_room3["Availability"].iloc[0]) + "</div>", unsafe_allow_html=True)
    col2.write("<div style='font-size: 18px; text-align: center;'><b>Date of Availability:</b> " + str(existing_data_room3["Date of Availability"].iloc[0]) + "</div>", unsafe_allow_html=True)
    col2.write(create_star_rating("star_room3", 0), unsafe_allow_html=True)

# Tab 4
with tab4:
    st.markdown("<h1 style='text-align: center;'>Room 4</h1>", unsafe_allow_html=True)
    st.markdown("<div style='display: flex; justify-content: center;'>", unsafe_allow_html=True)
    st.image("images/room2.jpg", caption='Sunrise by the mountains', width=2000)
    st.markdown("</div>", unsafe_allow_html=True)
    col1, col2 = st.columns(2)

    col1.write("<div style='font-size: 18px; text-align: center;'><b>Description:</b> " + str(existing_data_room4["Description"].iloc[0]) + "</div>", unsafe_allow_html=True)
    col2.write("<div style='font-size: 18px; text-align: center;'><b>Price:</b> ₱" + str(existing_data_room4["Price"].iloc[0]) + "</div>", unsafe_allow_html=True)
    col2.write("<div style='font-size: 18px; text-align: center;'><b>Availability:</b> " + str(existing_data_room4["Availability"].iloc[0]) + "</div>", unsafe_allow_html=True)
    col2.write("<div style='font-size: 18px; text-align: center;'><b>Date of Availability:</b> " + str(existing_data_room4["Date of Availability"].iloc[0]) + "</div>", unsafe_allow_html=True)
    col2.write(create_star_rating("star_room4", 0), unsafe_allow_html=True)

# Tab 5
with tab5:
    st.markdown("<h1 style='text-align: center;'>Room 5</h1>", unsafe_allow_html=True)
    st.markdown("<div style='display: flex; justify-content: center;'>", unsafe_allow_html=True)
    st.image("images/room1.jpg", caption='Sunrise by the mountains', width=2000)
    st.markdown("</div>", unsafe_allow_html=True)
    col1, col2 = st.columns(2)

    col1.write("<div style='font-size: 18px; text-align: center;'><b>Description:</b> " + str(existing_data_room5["Description"].iloc[0]) + "</div>", unsafe_allow_html=True)
    col2.write("<div style='font-size: 18px; text-align: center;'><b>Price:</b> ₱" + str(existing_data_room5["Price"].iloc[0]) + "</div>", unsafe_allow_html=True)
    col2.write("<div style='font-size: 18px; text-align: center;'><b>Availability:</b> " + str(existing_data_room5["Availability"].iloc[0]) + "</div>", unsafe_allow_html=True)
    col2.write("<div style='font-size: 18px; text-align: center;'><b>Date of Availability:</b> " + str(existing_data_room5["Date of Availability"].iloc[0]) + "</div>", unsafe_allow_html=True)
    col2.write(create_star_rating("star_room5", 0), unsafe_allow_html=True)

# Tab 6
with tab6:
    st.markdown("<h1 style='text-align: center;'>Room 6</h1>", unsafe_allow_html=True)
    st.markdown("<div style='display: flex; justify-content: center;'>", unsafe_allow_html=True)
    st.image("images/room2.jpg", caption='Sunrise by the mountains', width=2000)
    st.markdown("</div>", unsafe_allow_html=True)
    col1, col2 = st.columns(2)

    col1.write("<div style='font-size: 18px; text-align: center;'><b>Description:</b> " + str(existing_data_room6["Description"].iloc[0]) + "</div>", unsafe_allow_html=True)
    col2.write("<div style='font-size: 18px; text-align: center;'><b>Price:</b> ₱" + str(existing_data_room6["Price"].iloc[0]) + "</div>", unsafe_allow_html=True)
    col2.write("<div style='font-size: 18px; text-align: center;'><b>Availability:</b> " + str(existing_data_room6["Availability"].iloc[0]) + "</div>", unsafe_allow_html=True)
    col2.write("<div style='font-size: 18px; text-align: center;'><b>Date of Availability:</b> " + str(existing_data_room7["Date of Availability"].iloc[0]) + "</div>", unsafe_allow_html=True)
    col2.write(create_star_rating("star_room6", 0), unsafe_allow_html=True)


# Tab 7
with tab7:
    st.markdown("<h1 style='text-align: center;'>Room 7</h1>", unsafe_allow_html=True)
    st.markdown("<div style='display: flex; justify-content: center;'>", unsafe_allow_html=True)
    st.image("images/room1.jpg", caption='Sunrise by the mountains', width=2000)
    st.markdown("</div>", unsafe_allow_html=True)
    col1, col2 = st.columns(2)

    col1.write("<div style='font-size: 18px; text-align: center;'><b>Description:</b> " + str(existing_data_room7["Description"].iloc[0]) + "</div>", unsafe_allow_html=True)
    col2.write("<div style='font-size: 18px; text-align: center;'><b>Price:</b> ₱" + str(existing_data_room7["Price"].iloc[0]) + "</div>", unsafe_allow_html=True)
    col2.write("<div style='font-size: 18px; text-align: center;'><b>Availability:</b> " + str(existing_data_room7["Availability"].iloc[0]) + "</div>", unsafe_allow_html=True)
    col2.write("<div style='font-size: 18px; text-align: center;'><b>Date of Availability:</b> " + str(existing_data_room7["Date of Availability"].iloc[0]) + "</div>", unsafe_allow_html=True)
    col2.write(create_star_rating("star_room7", 0), unsafe_allow_html=True)
