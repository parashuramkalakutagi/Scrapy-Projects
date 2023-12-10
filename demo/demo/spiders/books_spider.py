from typing import Any
# from openpyxl.workbook import workbook
# import pandas as pd
import scrapy
from scrapy.http import Response
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider,Rule
from ..items import DemoItem

# extracting and storing data in data base


class Book_Spider(scrapy.Spider):
    name = 'book'
    start_urls = [
        'https://books.toscrape.com/catalogue/category/books/mystery_3/page-1.html'
    ]


    def parse(self, response: Response, **kwargs: Any) -> Any:

        items = DemoItem()

        book_name = response.css('h3 a::text').extract()
        price = response.css('p.price_color::text').extract()
        availability = response.css('.availability::text').extract()

        items['book_name'] = book_name
        items['price'] = price
        items['availability'] = availability


        yield items

class qutos_spider(scrapy.Spider):
    name = 'quotes'
    page_number = 2
    start_urls = [
        'https://quotes.toscrape.com/page/1/'
    ]

    def parse(self, response: Response, **kwargs: Any) -> Any:

        items = DemoItem()

        all_divs = response.css('div.quote')
        for tags in all_divs:
            name = tags.css('.text::text').extract()
            author = tags.css('.author::text').extract()
            tag = tags.css('.tag::text').extract()

            items['name'] = name
            items['author'] = author
            items['tag'] = tag

            yield items

        next_page = 'https://quotes.toscrape.com/page/'+ str(qutos_spider.page_number)+'/'

        if  qutos_spider.page_number < 11:
            qutos_spider.page_number+=1
            yield response.follow(next_page,callback=self.parse)

