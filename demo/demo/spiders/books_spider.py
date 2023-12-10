from typing import Any
# from openpyxl.workbook import workbook
# import pandas as pd
import scrapy
from scrapy.http import Response
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider,Rule
from ..items import DemoItem,DemoItems




class Book_Spider(scrapy.Spider):
    name = 'book'
    start_urls = [
        'https://books.toscrape.com/catalogue/category/books/mystery_3/page-1.html'
    ]


    def parse(self, response: Response, **kwargs: Any) -> Any:

        items = DemoItems()

        book_name = response.css('h3 a::text').extract()
        price = response.css('p.price_color::text').extract()
        availability = response.css('.availability::text').extract()

        items['book_name'] = book_name
        items['price'] = price
        items['availability'] = availability


        yield items

