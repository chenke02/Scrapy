# -*- coding: utf-8 -*-

#导入scrapy类库
import scrapy


class TaobaoItem(scrapy.Item):
    name = scrapy.Field()
    content = scrapy.Field()
    link = scrapy.Field()
    capacity = scrapy.Field()
    method = scrapy.Field()
    download = scrapy.Field()
    last_updated = scrapy.Field(serializer=str)