# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import codecs
import json
from scrapy.pipelines.images import ImagesPipeline
import MySQLdb

class ArticlespiderPipeline(object):
    def process_item(self, item, spider):
        return item

class MysqlPipeline(object):
    def __init__(self):
        self.conn = MySQLdb.connect('192.168.1.77', 'root', '1234ABcd', 'scrapyspider', charset='utf8', use_unicode = True)
        self.cursor = self.conn.cursor()

    def process_item(self, item, spider):
        insert_sql = """
            INSERT INTO article (url, title, image_url)
            VALUES (%s, %s, %s)
        """
        self.cursor.execute(insert_sql, (item["url"], item["title"], item["front_image_url"][0]))
        self.conn.commit()

class JsonWithEncodingPipeline(object):
    def __init__(self):
#        self.file = codecs.open('article.json', 'w', encoding="utf-8")

     def process_item(self, item, spider):
         lines = json.dumps(dict(item), ensure_ascii=False) + "\n"
         self.file.write(lines)
         return item

     def spider_closed(self, spider):
         self.file.close()

# class ArticleImagePipeline(ImagesPipeline):
#
