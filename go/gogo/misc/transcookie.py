# -*- coding: utf-8 -*-

class transCookie:
    def __init__(self, cookie):
        self.cookie = cookie

    def stringToDict(self):
        itemDict = {}
        items = self.cookie.split(';')
        for item in items:
            key = item.split('=')[0].replace(' ', '')
            value = item.split('=')[1]
            itemDict[key] = value
        return itemDict

if __name__ == "__main__":
    cookie = "gr_user_id=72a9ac5b-df76-497d-8f01-74654c5b2b8c; bid=KXEGX6gYPag; ps=y; ll="108288"; _ga=GA1.2.706977939.1485239741; _gid=GA1.2.1578897428.1519625801; __yadk_uid=qdJs5aFT1iCRDPITGzIYndyEpuj1h83c; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1519701667%2C%22https%3A%2F%2Fwww.douban.com%2F%22%5D; _vwo_uuid_v2=B396BAE95E90392DFAC07EDF8B29266E|613f1db5fdfbf7870ae460658e4953b5; ap=1; ck=8a8v; __utma=30149280.706977939.1485239741.1519699430.1519701684.53; __utmb=30149280.0.10.1519701684; __utmc=30149280; __utmz=30149280.1519701684.53.27.utmcsr=accounts.douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/login; __utmv=30149280.202; __utma=223695111.706977939.1485239741.1519699430.1519701684.4; __utmb=223695111.0.10.1519701684; __utmc=223695111; __utmz=223695111.1519701684.4.2.utmcsr=accounts.douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/login; _pk_id.100001.4cf6=6e9d61596cfd6231.1519628686.4.1519703177.1519699431.; _pk_ses.100001.4cf6=*; push_noty_num=0; push_doumail_num=0"
    trans = transCookie(cookie)
    print trans.stringToDict()
