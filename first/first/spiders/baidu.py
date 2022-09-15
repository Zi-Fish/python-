import scrapy


class BaiduSpider(scrapy.Spider):
    name = 'baidu'
    allowed_domains = ['http://www.baidu.com']
    start_urls = ['http://www.baidu.com/']

    def parse(self, response):
        print("百度一下")
