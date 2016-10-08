# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


# -*- coding: utf-8 -*-
import json
from scrapy import signals
import codecs
from os import path
from scrapy import signals
import sys  

reload(sys)  
sys.setdefaultencoding('utf-8') 

class NewsPipeline(object):
    def __init__(self):
		self.file = codecs.open('out.html', 'wb',"utf-8")
    def open_spider(self,spider):
		self.file.write("<html>")
		self.file.write("<meta charset='utf-8'>")
		self.file.write("<body>")
		self.file.write("<table  border='2'>")
		self.file.write("<tr height='70'>")
		self.file.write("<td width='280' valign='middle' align='center'><h3>名称</h3></td>")
		self.file.write("<td width='50' align='center' valign='middle'><h3>大小</h3></td>")
		self.file.write("<td width='50' align='center'><h3>类型</h3></td>")
		self.file.write("<td width='1100' align='center'><h3>游戏介绍</h3></td>")
		self.file.write("<td width='80' valign='middle' align='center'><h3>下载</3></td>")
    def process_item(self, item, spider):
		tm1=item['name'][0].decode('utf-8')
		tm2=u'\u300b'
		tm3=tm1.find(tm2)
		self.file.write("<tr height='70'>")
		self.file.write("<td width='280' valign='middle' align='center'><a href=%s><h4>" %json.dumps(item['link']))
		self.file.write("%s</h4></a></td>" %item['name'][0].decode('utf-8')[0:tm3+1].encode('utf-8'))
		self.file.write("<td width='50' align='center' valign='middle'><h5>%s</h5></td>" %item['capacity'][0])
		self.file.write("<td width='80' align='center' valign='middle'><h5>%s</h5></td>" %item['method'][0])
		self.file.write("<td width='1100' align='left'><h5>%s</h5></td>" %item['content'][0]+"\n")
		self.file.write("<td width='80' valign='middle' align='center'><a href=%s>" %item['download'][0])
		self.file.write("<h4>下载</4></a></td>")
		self.file.write("</tr>")
		self.file.write("</tr>")
		self.file.write("</tr>")
		return item
		file.close()
		
    def close_spider(self,spider):
		self.file.write("</table>")
		self.file.write("</body>")
		self.file.write("</html>")

