from lxml import html
import requests
from pprint import pprint
from pymongo import MongoClient

url = 'https://ru.ebay.com/b/Comic-Books-Manga-Memorabilia/63/bn_1865459'
header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36'}

response = requests.get(url, headers=header)

client = MongoClient('127.0.0.1', 27017)
db_comics = client['ebay_comics']
comics100821 = db_comics.comics100821

magazines = []
dom = html.fromstring(response.text)
items = dom.xpath("//li[contains(@class, 's-item')]")

for item in items:
    magazine = {}
    name = item.xpath(".//h3[@class='s-item__title']/text()")
    link = item.xpath(".//a[@class='s-item__link']/@href")
    price = item.xpath(".//span[@class='s-item__price']/text()")
    info = item.xpath(".//span[contains(@class, 's-item__hotness')]//text()")

    magazine['name'] = name
    magazine['link'] = link
    magazine['price'] = price
    magazine['info'] = info
    comics100821.insert_one(magazine)
    magazines.append(magazine)
print(len(magazines))
pprint(magazines)

