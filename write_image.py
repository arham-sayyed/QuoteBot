from PIL import Image, ImageDraw , ImageFont
from texts import *

def write(inp_image , inp_text):
    image = Image.open(inp_image)
    draw = ImageDraw.Draw(image)
    width , height = image.size
    text , smaller_strings = (breaker(inp_text)) # calling breaker 
    font_obj = fontCalcky(smaller_strings[0]) # directly getting the "font = ImageFont.truetype("arial.ttf", fontsize)"
    
    textwidth, textheight = draw.textsize(text, font=font_obj)
    x = (width - textwidth) / 2
    y = (height - textheight) / 2

    draw.text((x, y), text, (255, 255, 255), font=font_obj)
    image.save(inp_image)
