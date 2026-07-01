import qrcode
from datetime import datetime

def generate_qr(data, fill_color="black", back_color="white"):

    # Check for empty input
    if not data.strip():
        raise ValueError("Input cannot be empty.")

    # Create QR object
    qr = qrcode.QRCode(version=None,error_correction=qrcode.constants.ERROR_CORRECT_M,box_size=10,border=4)

    # Add data
    qr.add_data(data)

    # Generate QR layout
    qr.make(fit=True)

    # Create image
    img = qr.make_image(fill_color=fill_color,back_color=back_color)

    # Create filename
    filename = f"qr_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"

    # Save image
    img.save(filename)
