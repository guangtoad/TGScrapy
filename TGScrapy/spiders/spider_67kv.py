# -*- coding: utf-8 -*-

import urllib
import scrapy
from copy import deepcopy
import os
import sys
reload(sys) 
# sys.path.append('../')
sys.setdefaultencoding('utf-8')

from TGScrapy.items import PageItem
import spider_base

class Spider_67kv(scrapy.Spider):
    name = '67kv'
    # 设置爬取域
    allowed_domains = ['http://67kv.com']
    # 设置起始地址
    start_urls = ['http://67kv.com/t05/index.html']

    # 设置基础地址
    baseString = 'http://67kv.com'
    # 接受响应# 接受响应
    def parse(self, response):
        # 解析url
        # 获取当前页面下级URL
        url_list = response.xpath('//div[@id="channel"]//div[@class="content bord mtop"]//div[@class="typelist"]/ul//li//a/@href').extract()
        # 'http://192.168.1.171'
        base_url = self.baseString

        self.log(base_url)
        for url in url_list:   
            item = PageItem()
            item['name'] = 'asd'
            item['url'] = base_url + url
            item['detail_url'] = base_url + url
            self.log("-------------")
            self.log(item['detail_url'])
            self.log(item['url'])
            yield scrapy.Request(
                base_url + url,
                callback = self.parse_detail,
                meta={"item": item},
                dont_filter=True
            )
        # 爬取下一页
        brand = u'下一页'
        next_page = response.xpath('//a[contains(text(),"%s")]/@href' % (brand)).extract_first()
        next_page = base_url + next_page
        nextpageitem = PageItem()
        nextpageitem['name'] = 'asd'
        nextpageitem['url'] = base_url + next_page
        nextpageitem['detail_url'] = base_url + next_page
        if next_page is not None:
        	self.log('nextpage')
        	self.log(next_page)
           	yield scrapy.Request(
                next_page,
                callback=self.parse,
                meta={"item": nextpageitem},
                dont_filter=True
            )
    # 爬取内容
    def parse_detail(self, response):
		fileName = response.css('title::text').extract_first()
		str1 = ' - '        
        # tttxtItem = PicItem()
		fileName = fileName[0:fileName.find(str1)]
    	# divtitle = '' + fileName
		fileName = fileName + ".txt"
		# filename = 'ab.txt'
		self.log("parse_detail-------------")
		self.log(fileName)
		# txtPath = get_project_settings().get('TXT_STORE')
		# print('txtPath:' + txtPath)
		# if not os.path.exists(path):
			# os.makedirs(txtPath)
		# mydir = os.path.dirname(__file__)
		# mydir = os.path.join(MYDIR, 'txt')
		# filePath = os.path.join(mydir, fileName)
		with open(fileName, 'wb') as file:
			ps = response.xpath('//div[@id="view2"]//p//text()').extract()
			content = ''
			for p in ps:
				file.write(p + '\n')
				# self.log(p)
				# content = content + p + '\n'
				# file.write('\n\n' + fileName + '\n\n')
				# file.write(content)
			# file.write('\n')
			file.close()
        