import requests

clientId = "ac2895073db74d878d7f432feb920e66"
clientSecret = "3af3cd792c674420b0cbbfc41c752481"

auth_url = 'https://accounts.spotify.com/api/token'

data = {
    'grant_type': 'client_credentials',
    'client_id': clientId,
    'client_secret': clientSecret,
}

auth_response = requests.post(auth_url, data=data)
if auth_response:
    access_token = auth_response.json().get('access_token')

    base_url = 'https://api.spotify.com/v1/'
    headers = {
        'Authorization': 'Bearer {}'.format(access_token)
    }
    featured_playlists_endpoint = 'browse/featured-playlists/?limit=10'
    featured_playlists_url = ''.join([base_url,featured_playlists_endpoint])
    response = requests.get(featured_playlists_url,headers=headers)
    if response:
        playlists = response.json().get('playlists').get('items')
        playlist_ids = set()
        for pl in playlists:
            playlist_id = pl.get('name')
            playlist_ids.add(playlist_id)
        print(playlist_ids)
        