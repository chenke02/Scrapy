# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ProjectItem(scrapy.Item):
    name=scrapy.Field()
    link=scrapy.Field()
    download=scrapy.Field()
    size=scrapy.Field()
    method=scrapy.Field()
    content=scrapy.Field()
    img=scrapy.Field()