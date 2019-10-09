# -*- coding: utf-8 -*-
import scrapy
import requests
import re


class GithubSpider(scrapy.Spider):
    name = 'github'
    allowed_domains = ['github.com']
    start_urls = ['https://github.com/login']

    def parse(self, response):
        authenticity_token = get_authenticity_token(response)

        print(authenticity_token)
        pass

    def get_authenticity_token(self, response):
        return response.css("div.auth-form form input::attr(name=authenticity_token)").extract_first("")
