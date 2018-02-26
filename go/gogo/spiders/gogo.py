#encoding: utf-8
import re
import scrapy
from scrapy.contrib.linkextractors import LinkExtractor
from scrapy.contrib.spiders import CrawlSpider, Rule

from items import GogoItem

class GogoSpider(CrawlSpider):
    name = "gogo"
    allowed_domains = ["www.douban.com"]
    start_urls = ["https://movie.douban.com/explore#!type=movie&tag=%E7%83%AD%E9%97%A8&sort=recommend&page_limit=20&page_start=0"]

    rules = (
        Rule(LinkExtractor(allow=r"/explore#!type=movie&tag=%E7%83%AD%E9%97%A8&sort=recommend&page_limit=20&page_start=\d+"), 
            callback="parse_gogo", follow=True),
    )
    def parse_gogo(self, response):
        for sel in response.xpath("//*[@id="content"]/div/div[1]/div/div[4]/div"):
            item = GogoItem()
            name = sel.xpath(".//a[1]/p/strong/text()").extract()
            if name: item["name"] = name[0].strip()
#            url = sel.xpath(".//div[@class='title']/a/@href").extract()
#            if url: item["url"] = url[0].strip()
            yield item 

class GogoReviewSpider(CrawlSpider):
    name = "gogo_review"
    allowed_domains = ["www.douban.com"]
    start_urls = ["https://movie.douban.com/explore#!type=movie&tag=%E7%83%AD%E9%97%A8&sort=recommend&page_limit=20&page_start=0"]

    rules = (
        Rule(LinkExtractor(allow=r"/explore#!type=movie&tag=%E7%83%AD%E9%97%A8&sort=recommend&page_limit=20&page_start=\d+"),
            callback="parse_review", follow=True),
    )

    def parse_review(self, response):
        pass
