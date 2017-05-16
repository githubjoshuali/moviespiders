#encoding: utf-8
import re
import scrapy
from scrapy.contrib.linkextractors import LinkExtractor
from scrapy.contrib.spiders import CrawlSpider, Rule

from items import LjcjItem

class LjcjSpider(CrawlSpider):
    name = "ljcj"
    allowed_domains = ["bj.lianjia.com"]
    start_urls = ["http://bj.lianjia.com/chengjiao/ny1sf1lc1lc2lc3f1f2f5y2y3y4y1l2l1a2a1p2p1/"]

    rules = (
        Rule(LinkExtractor(allow=r"/chengjiao/\w+\/ny1sf1lc1lc2lc3f1f2f5y2y3y4y1pg\d+l2l1a2a1p2p1/"), 
            callback="parse_ljcj", follow=True),
    )
    def parse_ljcj(self, response):
        item = LjcjItem()

        housecount = int(response.xpath("//div[@class='resultDes clear']/div[@class='total fl']/span/text()"))
        if housecount: pagecount = housecount%30 + 1
        self.get_name(response, item)
        self.get_url(response,item)
        housecount = []
        pagecount = []

        return item

    def get_name(self, response, item):
        name = response.xpath("//ul[@class='listContent']/li[]/div[@class='info']/div[@class='title']/text()").extract()
        if name: item["name"] = name[0].strip()

    def get_url(self, response, item):
        url = response.xpath("//ul[@class='listContent']/li[]/div[@class='info']/div[@class='title']/a").extract()
        if url: item["url"] = url[0].strip()            

class LjcjReviewSpider(CrawlSpider):
    name = "ljcj_review"
    allowed_domains = ["bj.lianjia.com"]
    start_urls = ["http://bj.lianjia.com/chengjiao/"]

    rules = (
        Rule(LinkExtractor(allow=r"/chengjiao/\w+\.html"),
            callback="parse_review", follow=True),
    )

    def parse_review(self, response):
        pass
