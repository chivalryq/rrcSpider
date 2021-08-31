# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface

from scrapy.exceptions import DropItem

IMAGE_NUM_LIMIT = 2


class PricePipeline(object):
    vat_factor = 1.15

    def process_item(self, item, spider):
        if item['price']:
            if item['price_excludes_vat']:
                item['price'] = item['price'] * self.vat_factor
            return item
        else:
            raise DropItem("Missing price in %s" % item)


# class RrcPipeline(object):
#     def process_item(self,item, spider):
#         urls = item['image_net_urls']
#         image_urls = ['https:' + x for x in urls]
#         if len(image_urls) > IMAGE_NUM_LIMIT:
#             image_urls = image_urls[:IMAGE_NUM_LIMIT]
#         local_urls = []
#         count = 0
#         for url in image_urls:
#             if not url.endswith('jpg'):
#                 continue
#             resp = requests.get(url)
#             filename = os.path.join(IMAGES_STORE,
#                                     "_".join([item["name"], item["car_buy_time"], str(count)])) + '.jpg'
#             count += 1
#             unicode = str(base64.urlsafe_b64decode(resp.content))[-8:]  # no $ char
#             if unicode in unicode_group:
#                 raise DropItem("Anti-robot image")
#             else:
#                 unicode_group.add(unicode)
#
#             print("downloading image:" + filename)
#             with open(filename, 'wb') as jpg:
#                 jpg.write(resp.content)
#             local_urls.append(filename)
#         item['image_urls'] = local_urls
#         del item['image_net_urls']
#         return item

class RrcPipeline(object):
    def process_item(self, item, spider):
        del item['image_net_urls']
        return item
