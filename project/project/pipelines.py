# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
#导入json库
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
        self.file.write("<td width='300' valign='middle' align='center'><h3>名称</h3></td>")
        self.file.write("<td width='100' align='center' valign='middle'><h3>大小</h3></td>")
        self.file.write("<td width='100' align='center'><h3>类型</h3></td>")
        self.file.write("<td width='250' align='center' valign='middle'><h3>海报</h3></td>")
        self.file.write("<td width='1100' align='center'><h3>电影简介</h3></td>")
        self.file.write("<td width='150' valign='middle' align='center'><h3>下载</3></td>")

    def process_item(self, item, spider):

        tm1=item['name'][0].decode('utf-8')
        tm2=u'\xbb\r\n'
        tm3 = tm1.split(tm2)
        tm4=tm3[2]
        tm5=tm4.split(".")


        md1=item['size'][0].decode('utf-8')
        md4=u'\uff1a'
        md2=md1.split(md4)
        md3=md2[2]

        dy1=item['content'][0].decode('utf-8')
        dy2=u'<img'
        dy3=dy1.split(dy2)
        dy4=dy3[1]
        dy5=u'jpg">'
        dy6=dy4.split(dy5)

        self.file.write("<tr height='70'>")
        self.file.write("<td width='300' valign='middle' align='center'><a href=%s><h4>" %json.dumps(item['link']))
        self.file.write("%s</h4></a></td>" %tm5[0])
        self.file.write("<td width='100' align='center' valign='middle'><h5>%s</h5></td>" %md3)
        self.file.write("<td width='100' align='center' valign='middle'><h5>%s</h5></td>" %item['method'][0])
        self.file.write("<td width='250' align='center' valign='middle'><img height='300' width='250' src=%s></td>" %item['img'][0])
        self.file.write("<td height='150' width='1100' align='left'><h5>%s</h5></td>" %dy6[1]+"\n")
        self.file.write("<td width='150' valign='middle' align='center'><a href=%s>" %item['download'][0])
        self.file.write("<h4>下载</h4></a></td>")
        self.file.write("</tr>")
        self.file.write("</tr>")
        self.file.write("</tr>")
        return item

    def close_spider(self,spider):
        self.file.write("</table>")
        self.file.write("</body>")
        self.file.write("</html>")