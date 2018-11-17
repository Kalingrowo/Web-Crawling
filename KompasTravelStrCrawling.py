# -*- coding: utf-8 -*-
import scrapy


class KompastravelstrcrawlingSpider(scrapy.Spider):
    name = 'KompasTravelStrCrawling'
    allowed_domains = ['travel.kompas.com/travel-story']
    start_urls = ['http://travel.kompas.com/travel-story/']

    def parse(self, response):
        indexItem = response.css('div.article__list')
        
        if len(indexItem) > 0:
            # get data from page
            for item in indexItem:
                news_page_url = item.css('div.article__list__title > h3.article__title > a.article__link::attr(href)').extract_first()
                yield scrapy.Request(url=news_page_url, callback=self.parse_berita, dont_filter=True)
            
            # handling nextpage
            current_page = response.css('div.paging__item > a.paging__link--active::text').extract_first()    
            next_page_url =  response.urljoin(self.start_urls[0] + str(int(current_page) + 1))
            yield scrapy.Request(url=next_page_url, callback=self.parse, dont_filter=True)
            
        else:
            return
        
    def parse_berita(self, response):
        news = {
                'title' : response.css('h1.read__title::text').extract_first(),
                'author' : response.css('div.read__author > a::text').extract_first(),
                'news' : response.css('div.read__content > p::text').extract_first()        
        }
        yield news
        
