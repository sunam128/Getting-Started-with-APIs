import requests
#api url
url="https://official-joke-api.appspot.com/random_joke"
#send a request
response=requests.get(url)
#convert from json into a dictionary
data=response.json()
#display the output
print("Joke:")
print(data["setup"])
print("Punchline")
print(data["punchline"])