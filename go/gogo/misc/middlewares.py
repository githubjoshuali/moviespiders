#encoding: utf-8
from random import choice
from misc.helper import gen_bids
from scrapy.conf import settings

class CustomCookieMiddleware(object):
    def __init__(self):
        self.bids = gen_bids()

    def process_request(self, request, spider):
        request.headers["Cookie"] = 'bid="%s"' % choice(self.bids)


class CustomUserAgentMiddleware(object):
    def __init__(self, agents):
        self.agents = agents

    @classmethod
    def from_crawler(cls, crawler):
        return cls(crawler.settings.getlist('USER_AGENTS'))

    def process_request(self, request, spider):
#        ug = "Baiduspider"
#        request.headers["User-Agent"] = ug
#        ua  = random.choice(settings.get('USER_AGENTS'))
#        if ua:
#            request.headers.setdefault('User-Agent', ua)
        request.headers.setdefault('User-Agent', choice(self.agents))

class CustomHeadersMiddleware(object):
    def process_request(self, request, spider):
        request.headers["Accept-Language"] = "zh-CN,zh"

class CustomHttpProxyMiddleware(object):
    def process_request(self, request, spider):
        request.meta['proxy'] = settings.get('HTTP_PROXY')
