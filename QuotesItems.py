# -*- coding: utf-8 -*-
import scrapy


class QuotesitemsSpider(scrapy.Spider):
    name = 'QuotesItems'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com/']

    def parse(self, response):
        quotes = response.css('div.quote')
        for quote in quotes :
            item = {
                    'author_name' : quote.css('small.author::text').extract_first(),
                    'text' : quote.css('span.text::text').extract_first(),
                    'tags' : quote.css('a.tag::text').extract_first()
                    }
            yield item
        
