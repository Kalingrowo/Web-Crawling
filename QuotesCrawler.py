# -*- coding: utf-8 -*-
import scrapy


class QuotescrawlerSpider(scrapy.Spider):
    name = 'QuotesCrawler'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com/']

    def parse(self, response):
        yield {
                'author name ' : response.css('small.author::text').extract_first(),
                'text' : response.css('span.text::text').extract_first(),
                'tags' : response.css('a.tag::text').extract_first() 
        }
