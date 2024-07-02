import scrapy
from ..items import QuoteItem

class QuotesSpider(scrapy.Spider):
    name = "quotes"
    allowed_domains = ["quotes.toscrape.com"]
    start_urls = ["https://quotes.toscrape.com/"]

    def parse(self, response):
        items = QuoteItem()
        for quote in response.css('div.quote'):
            title = quote.css('span.text::text').get()
            author = quote.css('.author::text').get()
            tag = quote.css('.tag::text').getall()

            items['title'] = title
            items['author'] = author
            items['tag'] = tag
            yield items


        next_page = response.css('li.next a::attr(href)').get()
        if next_page:
            yield response.follow(next_page, self.parse)