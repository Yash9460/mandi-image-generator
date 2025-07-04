# from PIL import Image, ImageDraw, ImageFont
# image = Image.open("C:/Users/Yash.Bansal/Desktop/image2.png")
# draw = ImageDraw.Draw(image)    

# font_date = ImageFont.truetype("arial.ttf", 55)
# font_price = ImageFont.truetype("arial.ttf", 65)

# new_date = input("Enter the date (e.g., 2023-10-01): ")
# new_price = input("Enter the rate: ")

# date_position = (180, 1352)
# price_position = (662, 1350)

# black = (0, 0, 0)

# for offset in [(0,0), (1, 0), (0, 1), (1, 1)]:
#     draw.text((date_position[0] + offset[0], date_position[1] + offset[1]), new_date, font=font_date, fill=black)
    
    
# for offset in [(0,0), (1, 0), (0, 1), (1, 1)]:
#     draw.text((price_position[0] + offset[0], price_position[1] + offset[1]), new_price + "/-", font=font_price, fill=black)

# # draw.text(date_position, new_date, font=font_date, fill=black)
# # draw.text(price_position, new_price + "/-", font=font_price, fill=black)
# # image.save("output_image.png")
# image.show()    
# print("Image updated and saved as output_image.png")


import os
import streamlit as st
from PIL import Image, ImageDraw, ImageFont
from io import BytesIO

st.set_page_config(page_title="Mandi Rate Image Generator", layout="centered")
st.title("Mandi Rate Image Generator")
st.markdown("Enter the date and rate to generate a new image.")

st.markdown("### Enter the date and rate")
new_date = st.text_input("Enter the date (e.g., 2023-10-01):")
new_price = st.text_input("Enter the rate:")
if st.button("Generate Image"):
    if new_date and new_price:
        try:
            image = Image.open("image3.png").convert("RGB")
            draw = ImageDraw.Draw(image)
            FONT_PATH = os.path.join(os.path.dirname(__file__), "ARIAL.TTF")
            font_date = ImageFont.truetype(FONT_PATH, 55)
            font_price = ImageFont.truetype(FONT_PATH, 65)

            date_position = (180, 1373)
            price_position = (662, 1370)

            black = (0, 0, 0)

            for offset in [(0, 0), (1, 0), (0, 1), (1, 1)]:
                draw.text((date_position[0] + offset[0], date_position[1] + offset[1]), new_date, font=font_date, fill=black)
                draw.text((price_position[0] + offset[0], price_position[1] + offset[1]), new_price + "/-", font=font_price, fill=black)

            st.markdown("### Preview of the updated image")
            st.image(image, caption="Preview Image", use_container_width=True)
            buf = BytesIO()
            image.save(buf, format="PNG")
            byte_im = buf.getvalue()
            st.markdown("### Download the updated image")
            st.download_button("Download Updated Image", data=byte_im, file_name="updated_image.png", mime="image/png")
        except Exception as e:
            st.error(f"An error occurred: {e}")
