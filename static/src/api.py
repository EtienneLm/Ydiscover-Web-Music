import requests as req
import json

clientId = "ac2895073db74d878d7f432feb920e66"
clientSecret = "3af3cd792c674420b0cbbfc41c752481"

        
def getToken():
    auth_url = 'https://accounts.spotify.com/api/token'
    data = {'grant_type': 'client_credentials','client_id': clientId,'client_secret': clientSecret}
    res = req.post(auth_url, data=data)
    if res.status_code == 200:
        return res.json().get('access_token')

def getTracks(token, genres, limit=1):
    spotifyPath = "https://api.spotify.com/v1/search"

    request = f'{spotifyPath}?q=genre%3A{genres}&type=track&limit={limit}'

    res = req.get(request, headers={"Content-Type":"application/json", "Authorization":f"Bearer {token}"})

    data = json.loads(res.text)
    allTracks = []
    for track in data['tracks']['items']:
        allTracks.append(track['external_urls']['spotify'])
    return allTracks

def getAllEmbebs( urls):
    embedUrls = []
    for url in urls:
        embedUrls.append(getEmbeb(url))
    return embedUrls
        
def getEmbeb( url):
    splitedUrl = url.split("/")
    embedUrl = ""
    for id, val in enumerate(splitedUrl):
        embedUrl+=val
        if val == 'open.spotify.com':
            embedUrl += "/embed/"
        elif id < len(splitedUrl)-1:
            embedUrl += "/"
    return embedUrl



#<iframe style="border-radius:12px" src="https://open.spotify.com/embed/playlist/6BK2krum9Qbli37FN6VqvL?utm_source=generator" 
# width="100%" height="352" frameBorder="0" allowfullscreen="" allow="autoplay; clipboard-write; encrypted-media; fullscreen; 
# picture-in-picture" loading="lazy"></iframe>