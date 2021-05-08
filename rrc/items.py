# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class RrcItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    car_name=scrapy.Field()
    car_price=scrapy.Field()
    car_down_payment=scrapy.Field()
    car_info=scrapy.Field()
    car_buy_time=scrapy.Field()
    car_mileage=scrapy.Field()
    car_tax=scrapy.Field()
    car_fee=scrapy.Field()
    car_location=scrapy.Field()
    car_find=scrapy.Field()

    # 存放url的下载地址
    image_urls = scrapy.Field()
    image_name = scrapy.Field()
    # 图片的本地保存地址
    image_paths = scrapy.Field()
