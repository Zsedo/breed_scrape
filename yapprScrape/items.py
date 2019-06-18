# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class YapprItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    original_label = scrapy.Field()
    breed_id = scrapy.Field()
    group = scrapy.Field()
    english = scrapy.Field()
    french = scrapy.Field()
    german = scrapy.Field()
    spanish = scrapy.Field()
    section = scrapy.Field()
    subsection = scrapy.Field()
    date_of_acceptance = scrapy.Field()
    official_lang = scrapy.Field()
    date_of_publish = scrapy.Field()
    status = scrapy.Field()
    country = scrapy.Field()
    working_trial = scrapy.Field()