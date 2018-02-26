#encoding: utf-8
import re
import scrapy
from scrapy.contrib.linkextractors import LinkExtractor
from scrapy.contrib.spiders import CrawlSpider, Rule

from items import LjcjItem

class LjcjSpider(CrawlSpider):
    name = "ljcj"
    allowed_domains = ["bj.lianjia.com"]
    start_urls = ["http://bj.lianjia.com/chengjiao/chaoyangmenwai1/ny1sf1lc1lc2lc3f1f2f5y2y3y4y1l2l1a2a1p2p1/"]

    rules = (
        Rule(LinkExtractor(allow=r"/chengjiao/\w+/^ny1sf1lc1lc2lc3f1f2f5y2y3y4y1$\w{0,5}^l2l1a2a1p2p1/$"), 
            callback="parse_ljcj", follow=True),
    )
    def parse_ljcj(self, response):
        for sel in response.xpath("//ul[@class='listContent']/li"):
            item = LjcjItem()
            name = sel.xpath(".//div[@class='title']/a/text()").extract()
            url = sel.xpath(".//div[@class='title']/a/@href").extract()
            if name: item["name"] = name[0].strip()
            if url: item["url"] = url[0].strip()
            yield item 

class LjcjReviewSpider(CrawlSpider):
    name = "ljcj_review"
    allowed_domains = ["bj.lianjia.com"]
    start_urls = ["http://bj.lianjia.com/chengjiao/chaoyangmenwai1/ny1sf1lc1lc2lc3f1f2f5y2y3y4y1l2l1a2a1p2p1/"]

    rules = (
        Rule(LinkExtractor(allow=r"/chengjiao/\w+/^ny1sf1lc1lc2lc3f1f2f5y2y3y4y1$\w{0,5}^l2l1a2a1p2p1/$"),
            callback="parse_review", follow=True),
    )

    def parse_review(self, response):
        pass
