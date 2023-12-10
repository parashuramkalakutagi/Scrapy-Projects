from typing import Any

import scrapy
from scrapy.http import Response
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider
from ..items import AmazonItem



class Amazon_book_spider(scrapy.Spider):
    name = 'Abooks'

    start_urls = [
        'https://www.amazon.in/s?k=books'
    ]

    def parse(self, response: Response, **kwargs: Any) -> Any:
        item = AmazonItem()

        book_name = response.css('.a-size-medium.a-text-normal::text').extract()
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


