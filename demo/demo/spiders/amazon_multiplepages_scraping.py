from typing import Any
# from openpyxl.workbook import workbook
# import pandas as pd
import scrapy
from scrapy.http import Response
from scrapy.spiders import Rule,CrawlSpider
from scrapy.linkextractors import LinkExtractor


#scraping multiple pages data of flifcart

class AmzonSpider(scrapy.Spider):
    name = 'amazon'
    page_number = 2
    start_urls = [
        'https://www.flipkart.com/search?q=mobile&sid=tyy%2C4io&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_2_5_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_2_5_na_na_na&as-pos=2&as-type=RECENT&page=1'
    ]

    def parse(self, response: Response, **kwargs: Any) -> Any:
        all_divs = response.css('div._2kHMtA')

        for div in all_divs:
            mobile_name = div.css('._4rR01T::text').get()
            price = div.css('._1_WHN1::text').get()
            detail = div.css('.rgWa7D::text').get()
            image = div.css('._396cs4::attr(src)').get()
            price_off = div.css('._3tbKJL span::text').get()

            yield {
                'mobile_name':mobile_name,
                'price':price,
                'about':detail,
                'price_off':price_off,
                'mobile_image':image

            }

        next_page = 'https://www.flipkart.com/search?q=mobile&sid=tyy%2C4io&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_2_5_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_2_5_na_na_na&as-pos=2&as-type=RECENT&page='+str(AmzonSpider.page_number)+''
        print(next_page)
        if AmzonSpider.page_number < 31:
            AmzonSpider.page_number+=1
            yield response.follow(next_page, callback=self.parse)


class qutos_spider(scrapy.Spider):
    name = 'quote'
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

