import requests
import uuid
import datetime
import random
import urllib
from API_secrets import client_id

# Define the API endpoint with the access key
def getImage(query="universe"):
    try:
        # titles = ["motivation","inspiration","hope","determination","strength","courage","positive","optimism","success","achievement","adventure","dreams","goals","aspiration","beautiful scenery","sunrise","sunset","ocean","mountains","sky","nature","green","blossoms","flowers","butterflies","stars","planets","abstract","patterns","texture","grunge","minimalism","simplicity"]
        dark_color_titles = [    "Dark Night Sky",    "Dark Forest",    "Dark Mountains",    "Dark Waterfall",    "Dark Cityscape",    "Dark Beach",    "Dark Ocean",    "Dark Landscape",    "Dark Storm Clouds",    "Dark Sunset",    "Dark Abstract",    "Dark Skyline",    "Dark Nature",    "Dark Mood",    "Dark Nightscape"]

        if query == "random":
            query = random.choice(dark_color_titles)
        endpoint = "https://api.unsplash.com/photos/random"
        params = {
            "query": query,
            "count": "4",
            "orientation": "landscape",
            "featured": "true",
            "client_id": client_id,
            "w": 4896,
            "h": 3264
        }
        # Send the API request
        response = requests.get(endpoint , params=params)

        # Check the response status code
        if response.status_code == 200:
            # Parse the JSON data
            data = response.json()

            # Get the URL for the full-resolution image
            file_paths = []
            for image_data in data:
                image_url = image_data["urls"]["full"]
                file_path = download_image(image_url)
                print("Inspiring Image URL:", image_url)
                print(f"File path: {file_path}")
                file_paths.append(file_path)
            return file_paths
        else:
            print("Request failed with status code:", response.status_code)
            return False
    except Exception as e:
        print(f"exception at `getImage`: {e} ")
        return False


def download_image(image_url):
    try:
        # Generate a unique imageFilename based on a UUID and the current date-time stamp
        
        imageFilename = str(datetime.datetime.now().strftime("%Y-%m-%d_%H")) + "_" + str(uuid.uuid1()) + ".jpg"
        file_path = "images\\" + imageFilename
        urllib.request.urlretrieve(image_url, file_path)
        return file_path
    except Exception as e:
        print(f"Exception at `downloadimage`: {e}")

# print(getImage())