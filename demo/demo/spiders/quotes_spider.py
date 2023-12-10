from typing import Any
# from openpyxl.workbook import workbook
# import pandas as pd
import scrapy
from scrapy.http import Response
from scrapy.spiders import Rule,CrawlSpider
from scrapy.linkextractors import LinkExtractor


# class scrapy_quotes(scrapy.Spider):
#     name = 'quotes'
#     start_urls = [
#         'https://quotes.toscrape.com/tag/books/'
#     ]
#
#     def parse(self, response: Response, **kwargs: Any) -> Any:
#         Author_name  = response.css('small.author::text').extract()
#         about = response.css('span.text::text').extract()
#         # tags = response.css('a.tag::text').extract()
#         data = {
#             'Author_Names':Author_name,
#             'Book_title':about,
#         }
#         df = pd.DataFrame(data) # data dumping into excel sheet
#         df.to_excel('books.xlsx', index=False)
#         return data
#

#
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


class AmzonSpider(scrapy.Spider):
    name = 'amazon'
    # page_number = 2
    start_urls = [
        'https://www.flipkart.com/search?q=mobile&sid=tyy%2C4io&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_2_5_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_2_5_na_na_na&as-pos=2&as-type=RECENT'
        '&suggestionId=mobile%7CMobiles&requestId=41ed9b92-e14c-4e60-ab52-4c9bbd49f4f8&as-backfill=on&page=1'
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

        # next_page = 'https://www.flipkart.com/search?q=mobile&sid=tyy%2C4io&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_2_5_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_2_5_na_na_na&as-pos=2&as-type=RECENT'
        # '&suggestionId=mobile%7CMobiles&requestId=41ed9b92-e14c-4e60-ab52-4c9bbd49f4f8&as-backfill=on&page='+str(AmzonSpider.page_number)+''
        # print(next_page)
        # if AmzonSpider.page_number < 31:
        #     AmzonSpider.page_number+=1
        #     yield response.follow(next_page, callback=self.parse)