from typing import Any
# from openpyxl.workbook import workbook
# import pandas as pd
import scrapy
from scrapy.http import Response
from scrapy.spiders import Rule,CrawlSpider
from scrapy.linkextractors import LinkExtractor



# MULTIPLE PAGES SCRAPING DATA FUNCTION

class Scrapy_books(CrawlSpider):
    name = 'books'
    allowed_domains = ["toscrape.com"]
    start_urls = [
        "https://books.toscrape.com/"
    ]
    rules = (
        Rule(LinkExtractor(allow='catalogue/category')),
        Rule(LinkExtractor(allow='catalogue', deny='category') , callback='parse_item')
    )

    def parse_item(self,response):
        yield {
            'book_names':response.css('.product_main h1::text').get(),
            'prices':response.css('.price_color::text').get(),
            'avalibility':response.css('.availability ::text')[1].get().replace("\n","").replace(" ","")
        }


class Books_spider(scrapy.Spider):
    name = 'authors'
    start_urls = [
        'https://quotes.toscrape.com/tag/books/'

    ]

    def parse(self, response: Response, **kwargs: Any) -> Any:
        all_tags = response.css('div.quote')

        for quote in all_tags:
            title = quote.css('.text::text').extract()
            author = quote.css('.author::text').extract()
            tags = quote.css('.tag::text').extract()

            yield {
                'title':title,
                'author':author,
                'tags':tags
            }


