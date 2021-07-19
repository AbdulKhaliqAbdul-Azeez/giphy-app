import requests
import random
 
def getImageUrlFrom(gif_name):
    #cat = gif_name+" cat"
    half= [gif_name, "cat"]
    rand = random.choice(half)
    giphy_request_link = "https://api.giphy.com/v1/gifs/search?api_key=PIUIXIN36OgwPazg4C4fzP54lzLZmSrK&q="+rand+"&limit=25&offset=0&rating=g&lang=en"
    respone = requests.get(giphy_request_link).json()
    random_number= random.randrange(0,25)
    return respone["data"][random_number]["images"]["downsized_large"]["url"]
   