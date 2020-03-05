# -*- coding: utf-8 -*-
import scrapy
import linecache
class UploadheathSpider(scrapy.Spider):
    name = 'uploadheath'
    allowed_domains = ['ctgu.edu.cn']
    start_urls = ['http://yiqing.ctgu.edu.cn/wx/index/login.do']
    data = dict()
    cookies = dict()
    twice = 0
    def __init__(self, twice=None, *args, **kwargs):
        super(UploadheathSpider, self).__init__(*args, **kwargs)
        self.twice = int(twice)
    #登陆
    def parse(self, response):
        url = 'http://yiqing.ctgu.edu.cn/wx/index/loginSubmit.do'
        #此处填写用户账号密码
        data_list = linecache.getline('accounts.txt',self.twice).split(';')
        self.data['username'] = data_list[0]
        self.data['password'] = data_list[1]
        request = scrapy.FormRequest(url=url,formdata=self.data,callback=self.parse_page,dont_filter=True)
        yield  request

    #进入主界面
    def parse_page(self,response):
        request = scrapy.Request(url='http://yiqing.ctgu.edu.cn/wx/health/main.do',callback=self.parse_edit)
        yield request

    #进入信息修改界面
    def parse_edit(self,response):
        request = scrapy.Request(url='http://yiqing.ctgu.edu.cn/wx/health/toApply.do',callback=self.parse_token)
        yield request

    #获取需要上传的form数据，并上传
    def parse_token(self,response):
        token = response.xpath('/html/body/main/section/form/input[1]/@value').get()
        inputs = response.xpath('//input')
        information = dict()
        information2 = dict()
        key = ['ttoken', 'province', 'city', 'district', 'adcode', 'longitude', 'latitude', 'sfqz', 'sfys', 'sfzy', 'sfgl', 'status', 'sfgr', 'szdz', 'sjh', 'lxrxm', 'lxrsjh', 'sffr', 'sffy', 'sfgr', 'qzglsj', 'qzgldd', 'glyy', 'sffx']
        for input in inputs:
            information[input.xpath('./@name').get()] = input.xpath('./@value').get()
        for i in key:
            information2[i] = information[i]
        #修改数据紧急联系人姓名
        #information2['lxrxm'] = '王萧翔'
        #未知，需手动添加
        information2['mqzz'] = ''
        #修改信息，其他健康情况
        information2['qt'] = '一切正常'
        #修改信息 地址
        #information2['district'] = '孝南区'
        #information2['szdz'] = '湖北省 孝感市 孝南区'
        request = scrapy.FormRequest(url='http://yiqing.ctgu.edu.cn/wx/health/saveApply.do',formdata=information2,callback=self.parse_print)
        yield  request

    #打印返回信息，查看是否成功
    def parse_print(self,response):
        print(response.text)
