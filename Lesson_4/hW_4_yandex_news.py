from lxml import html
import requests
from pprint import pprint
from pymongo import MongoClient

client = MongoClient('127.0.0.1', 27017)
db_yandex_news = client['yandex_news']
yandex_news100821 = db_yandex_news.news100821

url = 'https://yandex.ru/news/'
header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36'}

response = requests.get(url, headers=header)

news_list = []
dom = html.fromstring(response.text)
news_items = dom.xpath("//div[@class='mg-grid__row mg-grid__row_gap_8 news-top-flexible-stories news-app__top']/div/article")
for news_item in news_items:
    news_one = {}
    news_title = news_item.xpath(".//div[@class='mg-card__inner']/a/h2/text() | .//div[@class='mg-card__text-content']/div/a/h2/text()")
    news_link = news_item.xpath(".//div[@class='mg-card__inner']/a/@href | .//div[@class='mg-card__text-content']/div/a/@href")
    news_one['news_title'] = news_title
    news_one['news_link'] = news_link

    footer_items = news_item.xpath(".//div[@class='mg-card-footer mg-card__footer mg-card__footer_type_image']")
    for footer_item in footer_items:
        news_own = footer_item.xpath(".//div[1]/div/span/a/text()")
        news_time = footer_item.xpath(".//div[1]/div/span[2]/text()")
        news_one['news_own'] = news_own
        news_one['news_time'] = news_time
    yandex_news100821.insert_one(news_one)
    news_list.append(news_one)
pprint(news_list)

