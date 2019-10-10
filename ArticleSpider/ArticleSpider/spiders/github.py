# -*- coding: utf-8 -*-
import scrapy

class GithubSpider(scrapy.Spider):
    name = 'github'
    allowed_domains = ['github.com']
    start_urls = ['https://github.com/login']

    def parse(self, response):
        authenticity_token = self.get_authenticity_token(response)
        ga_id = self.get_ga_id(response)
        webauthn_support = self.get_webauthn_support(response)
        webauthn_iuvpaa_support = self.get_webauthn_iuvpaa_support(response)
        required_field_68a0 = self.get_required_field_68a0(response)
        timestamp = self.get_timestamp(response)
        timestamp_secret = self.get_timestamp_secret(response)

        login_data = {
            'commit' : 'Sign in',
            'utf8' : '%E2%9C%93',
            'authenticity_token' : authenticity_token,
            'ga_id' : ga_id,
            'login' : 'maxnie87',
            'password' : 'nie920807',
            'webauthn-support' : webauthn_support,
            'webauthn-iuvpaa-support' : webauthn_iuvpaa_support,
            'required_field_e0be' : required_field_68a0,
            'timestamp' : timestamp,
            'timestamp_secret' : timestamp_secret
        }

        yield scrapy.FormRequest.from_response(response=response,
                                         url='https://github.com/session',
                                         formdata=login_data,
                                        callback =self.github_after
                                         )

    def github_after(self, response):
        list = response.xpath("//a[contains(@class, 'no-underline') and contains(@class, 'user-profile-link')]/@href").extract()
        if '/MaxNie87' in list:
            print('Login Success')
        else:
            print('Login Failed')

    def get_authenticity_token(self, response):
        return response.css("div.auth-form form input[name='authenticity_token']::attr(value)").extract_first("")

    def get_ga_id(self, response):
        return response.css("div.auth-form form input[name='ga_id']::attr(value)").extract_first("")

    def get_webauthn_support(self, response):
        return response.css("div.auth-form form div.auth-form-body input[name='webauthn-support']::attr(value)").extract_first("")

    def get_webauthn_iuvpaa_support(self, response):
         return response.css("div.auth-form form div.auth-form-body input[name='webauthn-iuvpaa-support']::attr(value)").extract_first("")

    def get_required_field_68a0(self, response):
         return response.css("div.auth-form form div.auth-form-body input[name='required_field_68a0']::attr(value)").extract_first("")

    def get_timestamp(self, response):
         return response.css("div.auth-form form div.auth-form-body input[name='timestamp']::attr(value)").extract_first("")

    def get_timestamp_secret(self, response):
         return response.css("div.auth-form form div.auth-form-body input[name='timestamp_secret']::attr(value)").extract_first("")
