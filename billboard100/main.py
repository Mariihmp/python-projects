from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import requests

# with open("webiste.html") as file:
#     contents = file.read()

# soup = BeautifulSoup(contents,'lxml')
# title = soup.title
# in_readable_mode = soup.prettify()#everything intended and easy to read
# all_achore_tag = soup.find_all(name="a")
# for tag in all_achore_tag:
#     tag.get('href')
#
# heading = soup.find(name='h1',id= 'name')
#
# company_url = soup.select_one(selector='p a')
# name = soup.select_one(selector='#name')
# soup.select('.heading')

# hacker_news_url = 'https://news.ycombinator.com'
# response = requests.get(hacker_news_url)
# yc_webpage = response.text
# #we want the title and the url to the news
#
# soup = BeautifulSoup(yc_webpage,"html.parser")
# article = BeautifulSoup(name='tr',class_='athing')
# print(article)

# empire_url = 'https://www.empireonline.com/movies/features/best-movies-2'
# response = requests.get(empire_url)
# website_html = response.text
# soup= BeautifulSoup(website_html,"html.parser")
# all_the_h3 = soup.find_all(name='h3',class_="listicleItem_listicle-item__title__hW_Kn")
#
#
#
#
# with open('titles.txt','w') as titles:
#     for h3 in all_the_h3[::-1]:
#         titles.write(f"{h3.get_text()}\n")





# response = requests.get(geniuse_endpoint,params=params_ge)
# response.raise_for_status()
#


#--------------------------------------------
date = input('which year do you want to travel to? in (yy-mm-dd) format')
billboard_url = "https://www.billboard.com/charts/hot-100/"+date



oauth_authorize_url = "https://accounts.spotify.com/authorize"
ouath_token_url = "https://accounts.spotify.com/api/token"

YOUR_APP_CLIENT_ID = 'bcec5d311fc14797adbd6155d1dab8ed'
YOUR_APP_CLIENT_SECRET = 'f9f51e58b0b24d749d4096adba5aa7bb'
YOUR_APP_REDIRECT_URI ='http://example.com'

import spotipy
from spotipy.oauth2 import SpotifyOAuth

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=YOUR_APP_CLIENT_ID,
                                               client_secret=YOUR_APP_CLIENT_SECRET,
                                               redirect_uri=YOUR_APP_REDIRECT_URI,
                                               scope="playlist-modify-private",
                                             ))

# user-library-read
results = sp.current_user()
USER_ID = results['mirhmp']
# print(USER_ID) you will need user id to create a playlist and add tracks!
response = requests.get(billboard_url)


soup = BeautifulSoup(response.text, 'html.parser')
song_list= soup.select('li ul li h3')
titles = [song.get_text().strip() for song in song_list]
uris = [sp.search(title)['tracks']['items'][0]['uri'] for title in titles]




# singer_names = soup.select('li ul li span')

year = date.split("-")[0]

PLAYLIST_ID = sp.user_playlist_create(user=USER_ID,public=False,name=f"{date} BillBoard-100")['id']

sp.playlist_add_items(playlist_id=PLAYLIST_ID,tracks=uris,user=USER_ID)


















