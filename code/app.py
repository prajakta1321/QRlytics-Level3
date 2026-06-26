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

# Description
st.write("Generate customizable QR codes and maintain generation history.")

# Input field
data = st.text_input("Enter text or URL")

# Color pickers
fill_color = st.color_picker("Choose QR color", "#000000")

back_color = st.color_picker("Choose background color", "#FFFFFF")

# Generate button
if st.button("Generate QR"):

    # Check empty input
    if not data.strip():

        st.error("Input cannot be empty.")

    else:

        try:

            # Generate QR
            filename = generate_qr(
                data,
                fill_color=fill_color,
                back_color=back_color
            )

            # Save details in database
            save_qr(
                data,
                fill_color,
                back_color,
                filename
            )

            # Success message
            st.success(
                f"QR generated successfully: {filename}"
            )

            # Preview image
            st.image(
                filename,
                caption="Generated QR Code"
            )

            # Download button
            with open(filename, "rb") as file:

                st.download_button(
                    label="Download QR",
                    data=file,
                    file_name=filename,
                    mime="image/png"
                )

        except Exception as e:

            st.error(f"Error: {e}")

st.header("QR History")

history = get_history()

if history:

    for row in history:

        st.write(f"ID: {row[0]}")

        st.write(f"Data: {row[1]}")

        st.write(f"QR Color: {row[2]}")

        st.write(f"Background Color: {row[3]}")

        st.write(f"Filename: {row[4]}")

        st.write(f"Created At: {row[5]}")

        st.divider()

else:

    st.info("No QR history available.")
