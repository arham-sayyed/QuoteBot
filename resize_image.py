from PIL import Image

def resize(image):
    try:
        im = Image.open(image)
        width , height = im.size
        new_width = 4896
        new_height = 3264
        # new_height = int(new_width * height / width)
        im = im.resize((new_width, new_height))
        im.save(image)
        im.close()
        return True
    except Exception as resize_error:
        im.close()
        print(f"resize error: {resize_error}")
        return False