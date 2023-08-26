import streamlit as st

# Set Streamlit app title and configuration
st.set_page_config(
    page_title="Homepage",
    page_icon="🌾",
    layout="wide",
)

# Set the app theme to "farmer" with green colors
st.markdown(
    """
    <style>
    .stApp {
        background-color: #f0f5e0;
        color: #374d20;
    }
    .stButton button {
        background-color: #7ab648;
        color: white;
    }
    .header {
        background-color: #f9df86;
        padding: 10px;
        display: flex;
        justify-content: space-between;
        align-items: center;
    }
    .header-button {
        background-color: #9cce4f;
        color: white;
        padding: 6px 12px;
        border-radius: 5px;
        margin: 0 10px;
    }
    .content {
        max-height: calc(100vh - 70px); /* Adjust this value as needed */
        overflow: auto;
        padding-bottom: 0; /* Remove bottom padding */
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Create the main layout
st.title("Farmers App")



# Display farmer's image
st.image("https://imgs.search.brave.com/UPipkIjGo1kIcO1yA1XSPqfFV1llUF1H0qjIZhcH2kI/rs:fit:860:0:0/g:ce/aHR0cHM6Ly90My5m/dGNkbi5uZXQvanBn/LzAwLzY5LzAyLzQy/LzM2MF9GXzY5MDI0/MjEwXzJKQXQ1VXJh/M0VUYWJUM0tWYjFT/TlBrUE5sV0RiTEtU/LmpwZw", use_column_width=True)

# Use a button to toggle content

