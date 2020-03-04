# -*- coding: utf-8 -*-
import scrapy

class UploadheathSpider(scrapy.Spider):
    name = 'uploadheath'
    allowed_domains = ['ctgu.edu.cn']
    start_urls = ['http://yiqing.ctgu.edu.cn/wx/index/login.do']
    cookies = dict()

    #登陆
    def parse(self, response):
        url = 'http://yiqing.ctgu.edu.cn/wx/index/loginSubmit.do'
        #此处填写用户账号密码
        data = {'username': '2016171122', 'password': '231314'}
        request = scrapy.FormRequest(url=url,formdata=data,callback=self.parse_page,dont_filter=True)
        yield  request

    #进入主界面
    def parse_page(self,response):
        request = scrapy.Request(url='http://yiqing.ctgu.edu.cn/wx/health/main.do',callback=self.parse_edit)
        yield request

    #进入信息修改界面
    def parse_edit(self,response):
        request = scrapy.Request(url='http://yiqing.ctgu.edu.cn/wx/health/editApply.do',callback=self.parse_token)
        yield request

    #获取需要上传的form数据，并上传
    def parse_token(self,response):
        token = response.xpath('/html/body/main/section/form/input[1]/@value').get()
        inputs = response.xpath('//input')
        information = dict()
        information2 = dict()
        key = ['ttoken', 'province', 'city', 'district', 'adcode', 'longitude', 'latitude', 'sfqz', 'sfys', 'sfzy', 'sfgl', 'status', 'sfgr', 'szdz', 'sjh', 'lxrxm', 'lxrsjh', 'sffr', 'sffy', 'qzglsj', 'qzgldd', 'glyy', 'sffx', 'mqzz', 'qt']
        for input in inputs:
            information[input.xpath('./@name').get()] = input.xpath('./@value').get()
        for i in key:
            information2[i] = information[i]
        #修改数据紧急联系人姓名
        information2['lxrxm'] = 'webdog'
        #未知
        information2['mqzz'] = '这是什么'
        #修改信息，其他健康情况
        information2['qt'] = '一切正常哈哈哈'
        #修改信息 地址
        information2['district'] = '孝南区'
        information2['szdz'] = '湖北省 孝感市 孝南区'
        request = scrapy.FormRequest(url='http://yiqing.ctgu.edu.cn/wx/health/saveApply.do',formdata=information2,callback=self.parse_print)
        yield  request

    #打印返回信息，查看是否成功
    def parse_print(self,response):
        print(response.text)