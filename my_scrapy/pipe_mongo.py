# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymongo
from scrapy.exceptions import DropItem


class Pipeline_mongo(object):
    def __init__(self, mongo_host, mongo_port):
        self.host = mongo_host
        self.port = mongo_port
        self.db_name = self.col_name = "beauty360"

    @classmethod
    def from_crawler(cls, crawler):
        # 依赖注入(构造对象,用来传入特定的参数) (setting中参数).返回一个类实例
        return cls(mongo_host=crawler.settings.get('MONGO_HOST'),
                   mongo_port=crawler.settings.get("MONGO_PORT"))

    def open_spider(self, spider):
        print("开启mongo数据库")
        self.conn = pymongo.MongoClient(host=self.host, port=self.port)
        self.db = self.conn[self.db_name]
        self.col = self.db[self.col_name]

    def process_item(self, item, spider):
        self.col.insert(dict(item))
        return item

    def close_spider(self, spider):
        print("关闭mongo数据库")
        self.conn.close()
