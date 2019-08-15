# -*- coding: utf-8 -*-
import scrapy
from urllib import parse
from scrapy.http import Request
from ArticleSpider.items import JianShuArticlespiderItem
from ArticleSpider.utils.common import get_md5


class JianshuSpider(scrapy.Spider):
    name = 'jianshu'
    allowed_domains = ['www.jianshu.com']
    start_urls = ['http://www.jianshu.com/']

    def parse(self, response):
        titles = response.css("div#list-container ul.note-list li div.content a.title::text").extract()
        post_elements = response.css("div#list-container ul.note-list li")
        for post_element in post_elements:
            #post_urls = post_element.css("div#list-container ul.note-list li div.content a.title::attr(href)").extract()
            post_url = post_element.css("div.content a.title::attr(href)").extract()[0]
            post_image_url = post_element.css("a.wrap-img img::attr(src)").extract_first("")
            front_end_url = parse.urljoin("https:", post_image_url)
            url = parse.urljoin(response.url, post_url)
            print(url)
            yield Request(url= url,meta={"front_end_url": front_end_url} , callback=self.parse_detail)

        # Extract urls in next page:
        next_page_sub_url = response.css("a.load-more::attr(href)").extract()
        next_url = parse.urljoin(response.url, next_page_sub_url)
        if next_page_sub_url:
            yield Request(url=parse(response.url, next_url), callback=self.parse)


    def parse_detail(self, response):
        front_end_url = response.meta["front_end_url"]
        title = response.xpath("//div[@class='post']/div[@class='article']/h1[@class='title']/text()").extract()[0]
        print(title)
        print(get_md5(response.url))
        jianshu_item = JianShuArticlespiderItem()

        jianshu_item["url"] = response.url
        jianshu_item["title"] = title
        jianshu_item['front_image_url'] = [front_end_url]

        yield jianshu_item
