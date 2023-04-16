from PIL import ImageFont

def breaker(my_string):
    try:
        global smaller_strings
        words = my_string.split()
        smaller_strings = []
        temp_string = ""
        string = ""
        for word in words:
            temp_string += (word + (" "))     
            # if len(temp_string.split()) > configure_breaker.words_limit:
            if len(temp_string.split()) > 12:
                smaller_strings.append(temp_string + "\n")
                temp_string = ""
        smaller_strings.append(temp_string)
        print(smaller_strings)
        return string.join(smaller_strings) , smaller_strings
    except Exception as e:
        print(f"string breaking error: {e}")


def fontCalcky(txt):
    try:
        image_width = 4896
        image_height = 3264
        img_fraction = 0.8

        fontsize = 1
        font = ImageFont.truetype("config\comic-sans-ms\ComicSansMSBold.ttf", fontsize)
        while font.getsize(txt)[0] < img_fraction*image_width:
            fontsize += 1
            font = ImageFont.truetype("config\comic-sans-ms\ComicSansMSBold.ttf", fontsize)
            # optionally de-increment to be sure it is less than criteria
        fontsize -= 2
        font = ImageFont.truetype("config\comic-sans-ms\ComicSansMSBold.ttf", fontsize)
        print(f"Finalized font size: {fontsize}")
        return font

    except Exception as e:
        print(f"error in font calcky: {e}")
        return False

# font_obj = fontCalcky(smaller_strings[0] , inp_image) # directly getting the "font = ImageFont.truetype("arial.ttf", fontsize)"

