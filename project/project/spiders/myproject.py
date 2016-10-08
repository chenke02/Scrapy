# -*- coding: utf-8 -*-

import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from project.items import ProjectItem
from scrapy.http import Request

class MySpider(scrapy.Spider):
    name = 'project'
    start_urls = ['http://www.mp4ba.com/index.php?cuid=B6B107F88DB0B970B9B6058A787EDF81%7Ccc43b95500000a&_client_version=7.1.6&nohead=1&page=1']

    #rules = [Rule(LinkExtractor(allow=(u'index.php\?.+&page=[1-9]?\d?\d$', ),),callback='parse_item',follow=True)]

    def parse(self,response):
        urls=response.xpath('//div[@class="clear"]/table[@id="listTable"]/tbody[@id="data_list"]//td[3]/a/@href').extract()

        for url in urls:
            url="http://www.mp4ba.com/"+url
            yield Request(url,callback=self.parse_content)
        #item['content']=response.xpath('').extract
        #item['download']=response.xpath('').extract

        next_urls=response.xpath("//div[@id='btm']/div[@class='main']/div[@class='pages clear']/a[last()]/@href").extract()
        for next_url in next_urls:
            next_url="http://www.mp4ba.com/"+next_url
            yield Request(next_url,callback=self.parse)

    def parse_content(self,response):
        item=ProjectItem()
        item['link']=str(response.url)
        item['name']=response.xpath("//div[@id='btm']/div[@class='location']").extract()
        item['size']=response.xpath("/html/body/div[@id='btm']/div[@class='main']/div[@class='slayout']/div[@class='inner']/div[@class='c2']/div[@class='box'][2]/h2[@class='title']/span[@class='right text_normal']").extract()
        item['method']=response.xpath("/html/body/div[@id='btm']/div[@class='location']/a[2]/text()").extract()
        item['img']=response.xpath("/html/body/div[@id='btm']/div[@class='main']/div[@class='slayout']/div[@class='inner']/div[@class='c2']/div[@class='box'][1]/div[@class='intro']/img[1]/@src").extract()
        item['content']=response.xpath("/html/body/div[@id='btm']/div[@class='main']/div[@class='slayout']/div[@class='inner']/div[@class='c2']/div[@class='box'][1]/div[@class='intro']").extract()
        item['download']=response.xpath("/html/body/div[@id='btm']/div[@class='main']/div[@class='slayout']/div[@class='inner']/div[@class='c1']/div[@class='box'][1]/div[@class='basic_info']/p[@class='original magnet']/a/@href").extract()
        yield item