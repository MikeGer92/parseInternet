from lxml import html
import requests
from pprint import pprint

url = 'https://www.ebay.com/b/Comic-Books-Manga-Memorabilia/63/bn_1865459'
header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36'}

response = requests.get(url, headers=header)

dom = html.fromstring(response.text)

names = dom.xpath("//h3[@class='s-item__title']/text()")

pprint(names)
