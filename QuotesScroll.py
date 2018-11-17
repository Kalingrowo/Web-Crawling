# -*- coding: utf-8 -*-
import scrapy
import json

class QuotesscrollSpider(scrapy.Spider):
    name = 'QuotesScroll'
    allowed_domains = ['quotes.toscrape.com']
    
    api_url = 'http://quotes.toscrape.com/api/quotes?page={page_num}'
    start_urls = [api_url.format(page_num=1)]

    def parse(self, response):
        data = json.loads(response.text)
        for quote in data['quotes']:
            yield {
                'author_name' : quote['author']['name'],
                'text' : quote['text'],
                'tag' : quote['tags']
            }
        
        if data['has_next']:
            next_page = data['page']+1
            yield scrapy.Request(url=self.api_url.format(page_num=next_page), callback=self.parse)
            
            
