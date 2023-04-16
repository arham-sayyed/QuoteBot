from json_parser import get_quote
from getBgImage import getImage
from write_image import write
from resize_image import resize

"""
  _         _   _       ____          ___ _   _ _ 
 | |    ___| |_( )___  |  _ \  ___   |_ _| |_| | |
 | |   / _ \ __|// __| | | | |/ _ \   | || __| | |
 | |__|  __/ |_  \__ \ | |_| | (_) |  | || |_|_|_|
 |_____\___|\__| |___/ |____/ \___/  |___|\__(_|_)
                                                  
"""

def main():
    # quote = "If you want to turn a vision into reality, you have to give \n 100% and never stop believing in your dream. "
    img_path = getImage(query="random") # returns a list of paths 
    for i in img_path:
      quote, author = get_quote()
      resize(i)
      write(i , quote)
    
# Rest in reason; move in passion. 
main()

