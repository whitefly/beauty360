# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class girlItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    girl_name = scrapy.Field()
    girl_postId = scrapy.Field()
    girl_url = scrapy.Field()
