# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Field, Item


class LjcjItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    subject_id = Field()
    name = Field()
#    cj_date = Field()
#    cj_price1 = Field() #成交价格
#    cj_price2 = Field() #成交单价
#    cj_day1 = Field() #成交周期（天）
#    gp_price1 = Field() #挂牌价格
#    hx_house = Field()
#    lc_house = Field() #所在楼层
#    mj_house1 = Field() #建筑面积
#    mj_house2 = Field() #套内面积
#    lx_house = Field() #建筑类型
#    cx_house = Field() #房屋朝向
#    nd_house = Field() #建成年代
#    zx_house = Field() #装修情况
#    jg_house = Field() #建筑结构
#    cq_house = Field() #产权年限
#    dt_house = Field() #配备电梯 
#    qs_house = Field() #交易权属
#    yt_house = Field() #房屋用途
#    nx_house = Field() #房屋年限
#    fq_hosue = Field() #房权所属 
#    pass
