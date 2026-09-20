import requests
#api url
url="https://catfact.ninja/fact"
#send a request
response=requests.get(url)
#convert from json into a dictionary
data=response.json()
#display the output
print("Cat fact:")
print(data["fact"])