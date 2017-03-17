# coding:utf-8

from scrapy.exceptions import DropItem
import json

class MyPipeline(object):
    def __init__(self):
        self.file = open('data.json', 'w', encoding='utf-8')
    # 处理数据
    def process_item(self, item, spider):
        #读取item中的数据
        line = json.dumps(dict(item), ensure_ascii=False) + "\n"
        self.file.write(line)
        return item
    
    def open_spider(self, spider):
        pass
    
    def close_spider(self, spider):
        pass