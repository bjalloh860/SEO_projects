import requests
import spotipy

CLIENT_ID = '839a8e46395b492e96807788b1ee97d0'
CLIENT_SECRET = 'ca5a5ccf5a8c47dbb94ed5b8fe905194'

AUTH_URL ='https://accounts.spotify.com/api/token'

# POST
auth_response = requests.post(AUTH_URL, {
    'grant_type': 'client_credentials',
    'client_id': CLIENT_ID,
    'client_secret': CLIENT_SECRET,
})

auth_response_data = auth_response.json()
access_token = auth_response_data['access_token']

# print(auth_response_data)

headers = {
    'Authorization': 'Bearer {}'.format(access_token)
}

BASE_URL = 'https://api.spotify.com/v1/'

# Track ID from the URI
# track_id_one  '6MO2bfLHKykUgCChFdw91H'
track_id_two = '6MO2bfLHKykUgCChFdw91H'

# actual GET request with proper header
r = requests.get(BASE_URL + 'audio-features/' + track_id_two, headers = headers)

r = r.json()
# print(r)

for k, v in r.items():
	print( k, ":", v)

