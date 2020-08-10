# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ShipSpiderItem(scrapy.Item):
    Name = scrapy.Field()
    Flag = scrapy.Field()
    MMSI = scrapy.Field()
    IMO = scrapy.Field()
    Call_Sign = scrapy.Field()
    Type = scrapy.Field()
    Size = scrapy.Field()
    Speed_AVG_or_MAX = scrapy.Field()
    Draught_AVG = scrapy.Field()
    GRT = scrapy.Field()
    DWT = scrapy.Field()
    Owner = scrapy.Field()
    Build = scrapy.Field()
