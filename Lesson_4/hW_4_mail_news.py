from lxml import html
import requests
from pprint import pprint
from pymongo import MongoClient

client = MongoClient('127.0.0.1', 27017)
db_news_mail = client['news_mail']
news_mail100821 = db_news_mail.news100821

url = 'https://news.mail.ru/'
header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36'}

response = requests.get(url, headers=header)

news_links_list = []
dom = html.fromstring(response.text)
items = dom.xpath("//div[@class='daynews__item daynews__item_big']/a/@href | //div[@class='daynews__item']/a/@href")
for item in items:
    news_one = {}
    include_response = requests.get(item,headers=header)
    include_dom = html.fromstring(include_response.text)
    title = include_dom.xpath("//h1/text()")
    news_link = item
    breadcrums = include_dom.xpath("//span[@class='note']/a/span[@class='link__text']/text()")
    news_time = include_dom.xpath("//span[@class='note__text breadcrumbs__text js-ago']/@datetime")
    news_one['title'] = title
    news_one['news_link'] = news_link
    news_one['breadcrums'] = breadcrums
    news_one['news_time'] = news_time
    news_mail100821.insert_one(news_one)
    print(news_one)



