import requests
response = requests.get("https://open.spotify.com/track/6gpcs5eMhJwax4mIfKDYQk?si=b6c4abe34ec84b71")
# print(response)

url = 'http://text-processing.com/api/sentiment/'
myobj = {'text': input()}

response = requests.post(url, data = myobj)

print(response.json())