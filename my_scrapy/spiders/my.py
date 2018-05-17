from urllib.parse import urlencode
from scrapy.http import Request
from scrapy import Spider
from my_scrapy.items import my_item
import json


class my_spider(Spider):
    name = "360beauty"

    def start_requests(self):
        data = {"ch": "beauty", "listtype": "new", "temp": 1}
        base_url = "https://image.so.com/zj?"
        for i in range(1, self.settings.get("MAX_PAGE") + 1):
            data['sn'] = 30 * i
            params = urlencode(data)
            real_url = base_url + params
            yield Request(real_url, callback=self.parse)

    def parse(self, response):
        # 转为json格式
        reuslt = json.loads(response.text)
        for image in reuslt.get('list'):
            item = my_item()
            item['title'] = image['group_title']
            item['id'] = image['id']
            item['thumb'] = image['qhimg_thumb_url']
            item['url'] = image['qhimg_url']
            yield item
