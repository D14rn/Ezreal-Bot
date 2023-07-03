from PIL import Image, ImageDraw, ImageFont, ImageEnhance
from io import BytesIO


async def welcome_image(interaction_user, bg_img=None, welcome_msg="Welcome to the server!"):
    with BytesIO() as img_buffer:
        await interaction_user.display_avatar.save(img_buffer)
        img = Image.open(img_buffer)
        enhancer = ImageEnhance.Brightness(img)
        img = enhancer.enhance(0.5)
        draw = ImageDraw.Draw(img)
        font = ImageFont.truetype("arial.ttf", 16)
        draw.text((30, 100), welcome_msg, "#BB0", font)
        draw.text((60, 120), interaction_user.global_name, "#BB0", font)
        return img
