import requests

from bs4 import BeautifulSoup

url = "https://www.bikewale.com/"

page = requests.get(url)

soup = BeautifulSoup(page.content, 'lxml')

print(soup)
