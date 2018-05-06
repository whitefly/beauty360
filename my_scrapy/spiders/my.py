from scrapy.http import Request
from scrapy import Spider
import re
from my_scrapy.items import girlItem
from bs4 import BeautifulSoup


class my_spider(Spider):
    name = "sky"
    start_urls = [
        'http://wizbw.top/forum-4.htm',
    ]

    def parse(self, response):
        soup = BeautifulSoup(response.text, "lxml")
        tags = soup.find_all("a", {"class": "subject breakall"})
        top_url = "http://wizbw.top/"
        # 解析1级页面试试
        for tag in tags:
            girl_url = top_url + tag.attrs["href"]
            yield Request(girl_url, callback=self.parse_detail)
        # 添加其他页面
        pat = re.compile("forum-4-.+?htm")
        urls = pat.findall(response.text)
        for new_url in urls:
            yield Request(top_url + new_url, callback=self.parse)

    def parse_detail(self, response):
        # 解析主播名字,日期,链接
        pat1 = re.compile("\[(.+?)\]\[(.+?)\]\[(.+?)\]")
        pat2 = re.compile(">\s*(magnet:.+?)<")

        res = pat1.search(response.text)
        my_item = girlItem()
        my_item["girl_name"] = res.group(1)
        my_item["girl_postId"] = res.group(2)
        res2 = pat2.search(response.text)
        my_item["girl_url"] = res2.group(1)
        return my_item
