# -*- coding: utf-8 -*-
import scrapy
from ScrapyDemo.items import ScrapydemoItem

class NewsspiderSpider(scrapy.Spider):
    name = 'NewsSpider'
    allowed_domains = ['news.baidu.com']
    start_urls = ['http://news.baidu.com/']

    def parse(self, response):
        for sel in response.xpath("//div[@id='pane-news']//li//a"):
            item = ScrapydemoItem()
            item["news_title"] = sel.xpath("text()").extract_first()
            item["news_url"] = sel.xpath("@href").extract_first()
            yield item
