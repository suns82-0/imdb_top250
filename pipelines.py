# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


from imdb.items import ImdbItem
import pymysql
from scrapy import log

from imdb import settings
from imdb.items import ImdbItem


class ImdbPipeline(object):
    def __init__(self):
        self.connect = pymysql.connect(
            host=settings.MYSQL_HOST,
            db=settings.MYSQL_DBNAME,
            user=settings.MYSQL_USER,
            passwd=settings.MYSQL_PASSWD,
            charset='utf8',
            use_unicode=True)
        self.cursor = self.connect.cursor()

    def process_item(self, item, spider):
        if item.__class__ == ImdbItem:
            try:
                self.cursor.execute("""INSERT INTO example_book_store (book_name, price)  
                        VALUES (%s, %s)""",
                       (item['book_name'].encode('utf-8'),
                        item['price'].encode('utf-8')))
                self.conn.commit()
            except Exception as error:
                log(error)
            return item
