# -*- coding: utf-8 -*-
# 导入scrapy类库
import scrapy
# 从taobao文件items类库导入TaobaoItem类
from taobao.items import TaobaoItem
from scrapy.http import Request

# 创建TaobaoSpider类继承于scrapy.spider类：spider类定义了如何爬取某个网站.
class TaobaoSpider(scrapy.Spider):
    name = "taobao"
    allowed_domains = []
    start_urls = ["http://down.ali213.net/pcgame/"]

    def parse(self, response):
        urls = response.xpath('//div[@class="list_body_con"]/a/@href').extract()
        for url in urls:
            url = "http://down.ali213.net/" + url
            yield Request(url,callback=self.parse_content)
        next_urls=response.xpath('//div[@class="list_body_page"]/a[11]/@href').extract()
        for next_url in next_urls:
            next_url = "http://down.ali213.net/"+next_url
            yield Request(next_url,callback=self.parse)

    def parse_content(self, response):
        item=TaobaoItem()
        item['link']=str(response.url)
        item['name']=response.xpath('//h1[@class="newdown_l_tit_cn"]/text()').extract()
        item['capacity']=response.xpath('//div[@class="newdown_l_con_con_info"]/span/text()').extract()
        item['method']=response.xpath('//div[@class="nydaohang"]/a[3]/text()').extract()
        item['content']=response.xpath('//div[@class="detail_body_con_bb_con1"]/p/text()').extract()
        item['download']=response.xpath('//div[@class="detail_down_adress_con_bottom_left_part1"]/div[2]/h4/a/@href').extract()
        yield item