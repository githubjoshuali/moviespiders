# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from misc.store import gogoDB

class GogoPipeline(object):
    def process_item(self, item, spider):
        if spider.name != "gogo":  return item
        if item.get("name", None) is None: return item

        spec = { "name": item["name"] }
        gogoDB.gogo.update(spec, {'$set': dict(item)}, upsert=True)

        return None
