# -*- coding: utf-8 -*-
import scrapy


class InfoqSpider(scrapy.Spider):
    name = 'infoq'
    allowed_domains = ['www.infoq.cn']
    start_urls = ['https://www.infoq.cn/article/VErbb1FMcSiC-uj5ZWU9']

    def parse(self, response):
        re_selector = response.xpath("/html/body/div[1]/div[2]/div[2]/div[2]/div[1]/h1")
        re_selector2 = response.xpath("//div[@class='article-main']/h1")
        pass
