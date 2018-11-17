# -*- coding: utf-8 -*-
import scrapy


class DetikpemilucrawlingSpider(scrapy.Spider):
    name = 'DetikPemiluCrawling'
    allowed_domains = ['detik.com/pemilu/indeks/']
    start_urls = ['http://detik.com/pemilu/indeks/']
    page = 1
    curr_date = '11/13/2018'

    def parse(self, response):
        indexItem = response.css('li.index__item')
        
        if len(indexItem) > 0:
            # get data from page
            for item in indexItem:
                news = {
                        'index__date' : item.css('span.index__date::text').extract_first(),
                        'index__title' : item.css('h2.index__title::text').extract_first()
                }
                yield news
            
            # handling nextpage
            current_page = response.css('div.paging_ > a.selected::text').extract_first()    
            next_page_url =  response.urljoin(self.start_urls[0] + 'artikel/' + str(int(current_page) + 1) + '?dt=' + self.curr_date)
            yield scrapy.Request(url=next_page_url, callback=self.parse, dont_filter=True)
            
        else:
            return
        
        
        
