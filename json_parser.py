import requests

def get_quote():
    try:
        endpoint = "https://zenquotes.io/api/random"
        response = requests.get(endpoint)

        if response.status_code == 200:
            data = response.json()
            quote = data[0]["q"]
            author = data[0]["a"]
            return quote, author
        else:
            print("Request failed with status code:", response.status_code)
            return False
    except Exception as e:
        print(f"Quote Error: {e}")
        return False


# quote, author = get_quote()

# print("Quote:", quote)
# print("Author:", author)
