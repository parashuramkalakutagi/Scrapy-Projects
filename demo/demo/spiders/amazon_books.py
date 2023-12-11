from typing import Any

import scrapy
from scrapy.http import Response
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider
from ..items import AmazonItem



class Amazon_book_spider(scrapy.Spider):
    name = 'Abooks'

    start_urls = [
        'https://www.amazon.in/s?k=books&rh=n%3A976389031%2Cn%3A23033695031&dc&ds=v1%3AXSXTz38nsdaNn5ERhIaiRQ4acpwlTwgUm05OXlA5jpk&qid=1702276554&rnid=3576079031&ref=sr_nr_n_2'
    ]

    def parse(self, response: Response, **kwargs: Any) -> Any:
        item = AmazonItem()

        book_name = response.css('.widgetId\=search-results_8 .a-spacing-mini , .widgetId\=search-results_8 .a-color-base.a-text-normal , .widgetId\=search-results_7 .a-color-base.a-text-normal , .widgetId\=search-results_6 .a-color-base.a-text-normal , .widgetId\=search-results_5 .a-color-base.a-text-normal , .widgetId\=search-results_4 .a-color-base.a-text-normal , .widgetId\=search-results_3 .a-color-base.a-text-normal , .widgetId\=search-results_1 .a-color-base.a-text-normal').css('::text').extract()
        author = response.css('.a-color-secondary.a-row.s-link-style::text').extract()
        price = response.css('.a-price-whole::text').extract()
        get_off = response.css('.widgetId\=search-results_22 .s-title-instructions-style .a-color-secondary .a-row , .a-color-base .a-letter-space+ span::text').extract()
        book_image = response.css('.s-image::attr(src)').extract()

        item['book_name'] = book_name,
        item['author'] = author
        item['price'] = price
        item['get_off'] = get_off
        item['book_image'] = book_image

        yield item


