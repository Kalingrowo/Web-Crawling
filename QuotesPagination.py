# -*- coding: utf-8 -*-
import scrapy


class QuotespaginationSpider(scrapy.Spider):
    name = 'QuotesPagination'
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
            
        # follow pahination link
        next_page_url = response.css('li.next > a::attr(href)').extract_first()
        if next_page_url :
            next_page_url = response.urljoin(next_page_url)
            yield scrapy.Request(url=next_page_url, callback=self.parse)
