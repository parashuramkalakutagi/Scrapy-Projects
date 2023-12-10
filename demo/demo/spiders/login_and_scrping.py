from typing import Any
# from openpyxl.workbook import workbook
# import pandas as pd
import scrapy
from scrapy.http import Response
from scrapy.spiders import Rule,CrawlSpider
from scrapy.linkextractors import LinkExtractor
from scrapy.http import FormRequest
from scrapy.utils.response import open_in_browser
#login and scraping data from website


class scrapy_quotes(scrapy.Spider):
    name = 'quotes'
    start_urls = [
        'https://quotes.toscrape.com/login'
    ]

    def parse(self, response: Response, **kwargs: Any) -> Any:
        token  = response.css('form input::attr(value)').get()
        return FormRequest.from_response(response,formdata={
            'csrf_token':token,
            'username':'parashuramkalakutagi@gmail.com',
            'password':'636363'
        },callback = self.strat_scraping)

    def strat_scraping(self,response):
        open_in_browser(response)

        all_divs = response.css('div.quote')
        for divs in all_divs:
            Author_name = divs.css('small.author::text').get()
            about = divs.css('span.text::text').get()
            tags = divs.css('a.tag::text').get()
            data = {
                'Author_Names': Author_name,
                'Book_title': about,
                'tags': tags
            }
            yield data




#
