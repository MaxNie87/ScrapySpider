# -*- coding: utf-8 -*-
import scrapy
import json
import base64
from io import BytesIO
from PIL import Image

class ZhihuSpider(scrapy.Spider):
    name = 'zhihu'
    allowed_domains = ['www.zhihu.com']
    start_urls = ['http://www.zhihu.com/']

    login_url = 'https://www.zhihu.com/api/v3/oath/sign_in'
    captcha_url = 'https://www.zhihu.com/api/v3/oauth/captcha?lang=en'

    def start_requests(self):
        yield scrapy.Request(url=self.captcha_url, callback=self.parse_get_captcha)

    def parse_get_captcha(self, response):
        is_captcha = json.loads(response.text).get("show_captcha")
        if is_captcha:
            yield scrapy.Request(url=self.captcha_url,method='PUT', callback=self.parse_image_url)

    def parse_image_url(self, response):
        img_url = json.loads(response.text).get("img_base64")

        img_data = base64.b64decode(img_url)

        img_real_url = BytesIO(img_data)
        img = Image.open(img_real_url)
        img.save('captcha.png')

        print("Please input verify code of Image.")

        result=input()

        yield scrapy.Request(
            url = self.captcha_url,
            callback=self.parse_post_captcha,
            formdata={
                'input_text': str(result)
            }
        )

    def parse_post_captcha(self, response):

        result = json.load(response.text).get("success", '')
        if result:
            post_data={
                'username':'17317925592',
                'password':'nie920807'
            }

            yield scrapy.FormRequest(
                url=self.login_url,
                formdata=post_data,
                callback=self.parse_login
            )