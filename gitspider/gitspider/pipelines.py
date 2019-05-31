# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json


class GitspiderPipeline(object):
    def __init__(self):
        # b表示二进制方式写入
        self.filename = open('tencent.json', 'wb')

    def process_item(self, item, spider):
        # 将item转为dict，再转为json格式。解码为utf-8后写入文件
        json_text = json.dumps(dict(item), ensure_ascii=False) + ',\n'
        self.filename.write(json_text.encode('utf-8'))
        return item

    def close_spider(self, spider):
        self.filename.close()
