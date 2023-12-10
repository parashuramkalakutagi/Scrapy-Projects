# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class DemoItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    author = scrapy.Field()
    tag = scrapy.Field()



class DemoItems(scrapy.Item):
    # define the fields for your item here like:
    book_name = scrapy.Field()
    price = scrapy.Field()
    availability = scrapy.Field()



class AmazonItem(scrapy.Item):
    # define the fields for your item here like:
    book_name = scrapy.Field()
    author = scrapy.Field()
    price = scrapy.Field()
    get_off = scrapy.Field()
    book_image  = scrapy.Field()
