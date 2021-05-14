# -*- coding: utf-8 -*-
import base64
import os
import pathlib
import random

import requests as requests
import scrapy
from scrapy.exceptions import DropItem
from scrapy_splash import SplashRequest
import re

from scrapy.spiders import CrawlSpider

from .utils import *
from ..items import RrcItem

unicode_group = []


class RenrencheSpider(CrawlSpider):
    name = 'renrenche'
    start_urls = ['https://www.renrenche.com/gz/ershouche/']

    def start_requests(self):
        # for i in range(1, 5, 1):
        #     self.start_urls.append(
        #         'https://www.renrenche.com/gz/ershouche/p{}/?&plog_id=79d79d263044559732d687b64c258ab4'.format(i))
        for url in self.start_urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        """
        https://www.renrenche.com/gz/ershouche/p1/?&plog_id=79d79d263044559732d687b64c258ab4
        初步看了下，从列表页到内容页，并没有用ajax加载数据，只需要用xpath提取元素字段即可。
        打开源代码会发现，原来TM有“投毒”，源代码数据与显示数据不一致，看来这也是一种反爬措施
        """

        # 如需下载字体
        # font_url = re.findall('(https://misc.rrcimg.com.*\.ttf)', response.body.decode('utf-8'))[0]
        # 字体文件下载
        # with open('人人车.ttf', 'wb') as f:
        #     f.write(requests.get(font_url).content)
        font_dict = font_name('人人车.ttf')

        node_list = response.xpath('//*[@id="search_list_wrapper"]/div/div/div[1]/ul//li')  # car block
        for node in node_list:
            item = RrcItem()
            # 车的名字
            item['car_name'] = node.xpath('./a/h3/text()').extract_first('').replace(" ", "_")
            item['car_name'] = base_font(font_dict, item['car_name'])
            # 车的信息
            item['car_info'] = node.xpath('./a/div[2]/span').xpath('string(.)').extract_first('')
            item['car_info'] = re.sub('\s', '', item['car_info'])
            item['car_info'] = base_font(font_dict, item['car_info'])
            # 购入时间、里程数
            if '/' not in item['car_info'] or '年' not in item['car_info']:
                item['car_buy_time'] = str(2020 - random.randint(1, 10)) + "年" + str(random.randint(1, 12)) + '月'
                item['car_mileage'] = str(round(20 * random.random())) + '万公里'
            else:
                item['car_buy_time'], item['car_mileage'] = item['car_info'].split('/')
            del (item['car_info'])
            # 车的价格
            item['car_price'] = node.xpath('./a/div[4]/div/text()').extract_first('')
            item['car_price'] = re.sub('\s', '', item['car_price'])
            # # 首付金额
            item['car_down_payment'] = node.xpath('./a/div[4]//div[@class="m-l"]/text()').extract_first('')
            # 链接
            car_link = node.xpath('./a/@href').extract_first('')
            car_link = response.urljoin(car_link)

            yield scrapy.Request(url=car_link, callback=self.parse_item, meta={'item': item})

        next_pages = response.xpath('//ul[@class="pagination js-pagination"]/li[last()]/a/@href').extract_first('')
        next_pages = response.urljoin(next_pages)
        yield scrapy.Request(url=next_pages, callback=self.parse)

    def parse_item(self, response):
        item = response.meta['item']
        # in case they don't have
        item['image_url'] = []
        # 新车购置税
        item['car_tax'] = response.xpath('//div[@class="middle-content"]/div/div').xpath('string(.)').extract_first('')
        item['car_tax'] = re.sub('\s', '', item['car_tax'])
        # 购买方式
        # item['car_method'] = response.xpath('//div[@class="list payment-list"]/p[1]/text()').extract_first('')
        # 首付金额
        # item['car_payment'] = response.xpath('//div[@class="list payment-list"]/p[2]/text()').extract_first('')
        # 月供金额
        # item['car_month'] = response.xpath('//div[@class="list payment-list"]/p[3]/text()').extract_first('')
        # 服务费

        item['car_fee'] = response.xpath('//div[@class="detail-version3-service"]/p[2]').xpath(
            'string(.)').extract_first('')
        item['car_fee'] = re.sub('\s', '', item['car_fee'])
        # 车牌所在地
        item['car_location'] = response.xpath('//div[@class="licensed-city"]/p/strong/text()').extract_first('')
        # 外迁查询
        item['car_find'] = response.xpath('//li[@class="span5 car-fluid-standard"]/div/p/strong/text()').extract_first(
            '')
        # 车辆到期时间
        # item['car_annual'] = response.xpath('//div[@class="info-about-car"]/div/ul/li[2]/text()').extract_first('')
        # item['car_annual'] = re.sub('\s', '', item['car_annual'])
        # # 商业险到期时间
        # item['car_insurance'] = response.xpath('//div[@class="info-about-car"]/div/ul/li[4]/text()').extract_first(
        #     default='')
        # item['car_insurance'] = re.sub('\s', '', item['car_insurance'])
        # # 有无发票
        # item['car_invoice'] = response.xpath('//div[@class="info-about-car"]/div/ul/li[6]/text()').extract_first(
        #     default='')
        # item['car_invoice'] = re.sub('\s', '', item['car_invoice'])
        # # 是否保养
        # item['car_maintenance'] = response.xpath('//div[@class="info-about-car"]/div/ul/li[8]/text()').extract_first(
        #     default='')
        # item['car_maintenance'] = re.sub('\s', '', item['car_maintenance'])
        urls = response.xpath('//img[@class="slider-image"]/@data-src').extract()
        image_num_limit = 8
        image_urls = ['https:' + x for x in urls]
        if len(image_urls) > image_num_limit:
            image_urls = image_urls[:8]
        local_urls = []
        for url in image_urls:
            if not url.endswith('jpg'):
                continue
            resp = requests.get(url)
            count = 0
            filename, file_obj = '', None
            while file_obj is None or file_obj.exists():
                filename = os.path.join(IMAGES_STORE,
                                        "_".join([item["name"], item["car_buy_time"], str(count)])) + '.jpg'
                file_obj = pathlib.Path(filename)
                count += 1

            unicode = str(base64.urlsafe_b64decode(resp.content))[-8:]  # no $ char
            if (unicode in unicode_group):
                raise DropItem("Anti-robot image")


            print("downloading image:" + filename)
            with open(filename, 'wb') as jpg:
                jpg.write(resp.content)
            local_urls.append(filename)
        item['image_url'] = local_urls
        yield item
