import qrcode
from PIL import Image, ImageDraw, ImageFont

def generate_qr(phone_number, file_name, text, text_font_size):
    # Create a QR Code instance
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )

    # Add data (phone number) to the QR Code
    qr.add_data(f"tel:{phone_number}")
    qr.make(fit=True)

        # Create an image from the QR Code instance
    img = qr.make_image(fill='aqua', back_color='orange')

        # Resize the image to make edges smoother
    base_size = 500  # Base size for smoother edges
    img = img.resize((base_size, base_size), Image.Resampling.LANCZOS)

       # Load a font
    try:
        font = ImageFont.truetype("arial.ttf", 20)
    except IOError:
        font = ImageFont.load_default()
    # Prepare to draw text on the image
    draw = ImageDraw.Draw(img)

   # Calculate text size and position
    text_bbox = draw.textbbox((0, 0), text, font=font)
    text_width = text_bbox[2] - text_bbox[0]
    text_height = text_bbox[3] - text_bbox[1]
    qr_width, qr_height = img.size
    text_x = (qr_width - text_width) / 2
    text_y = qr_height - text_height - 10
        
    # Draw the text on the image
    draw.text((text_x, text_y), text, font=font, fill='black')

    # Save the image
    img.save(file_name)

if __name__ == "__main__":
    phone_number = input("Enter the phone number (include country code if applicable): ")
    file_name = input("Enter the file name to save the QR code (e.g., phone_qr.png): ")
    text = input("Enter the text that will appear with the  QR Code: ")
    generate_qr(phone_number, file_name, text, text_font_size=400)
    print(f"QR code saved as {file_name}")
