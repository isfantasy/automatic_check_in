# -*- coding: utf-8 -*-
'''
Author: Fantasy
Date: 2020-10-31 19:21:52
LastEditors: Fantasy
LastEditTime: 2020-10-31 22:21:45
Descripttion: 
Email: 776474961@qq.com
'''
import scrapy
from scrapy.utils.project import get_project_settings
import re


class UploadheathSpider(scrapy.Spider):
    name = 'uploadheath'
    allowed_domains = ['ctgu.edu.cn']
    login_url = 'http://yiqing.ctgu.edu.cn/wx/index/loginSubmit.do'
    apply_url = 'http://yiqing.ctgu.edu.cn/wx/health/toApply.do'
    sava_url = 'http://yiqing.ctgu.edu.cn/wx/health/saveApply.do'

    def start_requests(self):
        settings = get_project_settings()
        for account_t in settings.get('ACCOUNTS'):
            account = {}
            account['username'] = account_t[0]
            account['password'] = account_t[1]
            yield scrapy.FormRequest(url=self.login_url,
                                     formdata=account,
                                     meta={'account': account},
                                     callback=self.check_login,
                                     dont_filter=True)

    # 检查是否登陆成功
    def check_login(self, response):
        account = response.meta['account']
        if 'success' == response.text:
            print("用户 {} 登陆成功".format(account['username']))
            yield scrapy.Request(url=self.apply_url,
                                 callback=self.apply_info_extract,
                                 meta={'account': account},
                                 dont_filter=True)
        elif 'fail' == response.text:
            print("用户 {} 密码错误，请修改配置文件".format(account))
        else:
            print("未知错误：")
            print(response.text)

    # 表单信息提取
    def apply_info_extract(self, response):
        account = response.meta['account']
        if re.findall(r'修改', response.text):
            print("用户 {} 今日已上报过".format(account['username']))
            return
        inputs = response.xpath('//input')
        form_data = {}
        for inp in inputs:
            form_data[inp.xpath('./@name').get()] = inp.xpath('./@value').get()
        form_data.pop(None)
        yield scrapy.FormRequest(url=self.sava_url,
                                 formdata=form_data,
                                 meta={'account': account},
                                 callback=self.check_save)

    # 检查是否上报成功
    def check_save(self, response):
        account = response.meta['account']
        if re.findall(r'true', response.text):
            print("用户 {} 上报成功".format(account['username']))
        else:
            print("用户 {} 上报失败：".format(account['username']))
            print(response.text)
