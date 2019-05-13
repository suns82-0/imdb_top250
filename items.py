# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ImdbItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    movie_name = scrapy.Field()
    director = scrapy.Field()
    score = scrapy.Field()
    actors = scrapy.Field()
    year = scrapy.Field()
    movie_id = scrapy.Field()
    pass
