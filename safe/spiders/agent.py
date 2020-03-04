# -*- coding: utf-8 -*-
import scrapy


class AgentSpider(scrapy.Spider):
    name = 'agent'
    allowed_domains = ['ctgu.edu.cn']
    start_urls = ['http://yiqing.ctgu.edu.cn/wx/index/logout.do']

    def parse(self, response):
        r = response.text
        print(r)

