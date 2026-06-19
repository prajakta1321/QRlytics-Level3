# Import Streamlit
import streamlit as st

# Import QR generator
from qr_generator import generate_qr

# Import database functions
from database import create_table
from database import save_qr
from database import get_history

# Create database table
create_table()

# Configure page
st.set_page_config(page_title="SmartQR",page_icon="")

# App title
st.title("SmartQR - Level 3")
