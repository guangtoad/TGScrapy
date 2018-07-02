# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class TgscrapyItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class PageItem(scrapy.Item):
    detail_url = scrapy.Field()
    url = scrapy.Field()
    name = scrapy.Field()
    pass

class TextItem(scrapy.Item):
	# 文本名称
	name = scrapy.Field()
	# 文本内容
	context = scrapy.Field()
	# 保存路径
	path = scrapy.Field()
	pass
	
class PicItem(scrapy.Item):
	# 名称
	name = scrapy.Field()
	# 图片URL
	url = scrapy.Field()
	# 保存路径
	path = scrapy.Field()
	# 文件名
	fileName = scrapy.Field()
	# 扩展名
	extension = scrapy.Field()
	pass    