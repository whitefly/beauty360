# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymongo


class MyScrapyPipeline(object):
    def __init__(self):
        self.port = 27017
        self.host = 'localhost'
        self.conn = pymongo.MongoClient(host=self.host, port=self.port)
        self.db = self.conn["korean"]
        self.col = self.db["girls"]

    def process_item(self, item, spider):
        name = item["girl_name"]
        id = item["girl_postId"]
        url = item["girl_url"]
        dic = {"name": name, "date": id, "down_url": url}
        self.col.insert(dic)
        return  item

    def __del__(self):
        self.conn.close()
