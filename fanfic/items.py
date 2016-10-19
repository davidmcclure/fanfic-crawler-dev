# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class BookIdItem(scrapy.Item):
    book_id = scrapy.Field()


class BookMetadataItem(scrapy.Item):
    title = scrapy.Field()
    username = scrapy.Field()
    summary = scrapy.Field()
    rated = scrapy.Field()
    genres = scrapy.Field()
    characters = scrapy.Field()
    favs = scrapy.Field()
    follows = scrapy.Field()
    published = scrapy.Field()
