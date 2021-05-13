# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import os.path
import pathlib
import time

from itemadapter import ItemAdapter
from scrapy import Request
from scrapy.exceptions import DropItem
from scrapy.pipelines.images import ImagesPipeline




class RrcPipeline(ImagesPipeline):
    def open_spider(self, spider):
        print("start crawling")

    def get_media_requests(self, item, info):
        for image_url in item['image_urls']:
            yield Request(image_url, meta={'item': item})

    def file_path(self, request, response=None, info=None, *, item=None):
        item = request.meta['item']
        print(item['car_name'])
        file_name = os.path.join(item['car_name'] + time.time())  # 修改图片文件的保存路径
        return file_name

    def item_completed(self, results, item, info):
        image_paths = [x['path'] for ok, x in results if ok]
        if not image_paths:
            raise DropItem("Item contains no files")
        item['image_paths'] = image_paths
        return item
