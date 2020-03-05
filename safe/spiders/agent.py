# -*- coding: utf-8 -*-
import scrapy
import linecache

class AgentSpider(scrapy.Spider):
    name = 'agent'
    allowed_domains = ['ctgu.edu.cn']
    start_urls = ['http://yiqing.ctgu.edu.cn/wx/index/logout.do']
    username = ''
    password = ''
    data = dict()
    twice = 1
    def __init__(self,twice = None, *args, **kwargs):
        super(AgentSpider, self).__init__(*args, **kwargs)
        self.twice = int(twice)

    def parse(self, response):
        str = linecache.getline('accounts.txt',self.twice).strip()
        print(str)
        print(type(self.twice))
