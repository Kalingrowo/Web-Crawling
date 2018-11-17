# -*- coding: utf-8 -*-
import scrapy


class QuotesloginSpider(scrapy.Spider):
    name = 'QuotesLogin'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com/login']

    def parse(self, response):
        return scrapy.FormRequest.from_response(
                response,
                formdata={'username' : 'admin', 'password' : 'admin'},
                callback=self.parse_quotes
        )

    def parse_quotes(self, response):
        for q in response.css('div.quote'):
            yield {
                    'author_name' : q.css('small.author::text').extract_first(),
                    'author_url' : q.css('small.author ~ a[href*="goodreads.com"]::attr(href)').extract_first()
            }