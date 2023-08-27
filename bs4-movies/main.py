from bs4 import BeautifulSoup
import lxml
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

empire_url = 'https://www.empireonline.com/movies/features/best-movies-2'
response = requests.get(empire_url)
website_html = response.text
soup= BeautifulSoup(website_html,"html.parser")
all_the_h3 = soup.find_all(name='h3',class_="listicleItem_listicle-item__title__hW_Kn")




with open('titles.txt','w') as titles:
    for h3 in all_the_h3[::-1]:
        titles.write(f"{h3.get_text()}\n")




