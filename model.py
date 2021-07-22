import requests
import random
 
def getImageUrlFrom(gif_name, key):
    giphy_request_link = f"https://api.giphy.com/v1/gifs/search?api_key={key}&q="+gif_name+"&limit=100&offset=0&rating=g&lang=en"
    respone = requests.get(giphy_request_link).json()
    random_number= random.randrange(0,25)
    return respone["data"][random_number]["images"]["downsized_large"]["url"]
   