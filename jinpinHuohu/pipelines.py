# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.pipelines.images import ImagesPipeline
import scrapy
import os
from jinpinHuohu.settings import IMAGES_STORE as images_store

class JinpinhuohuPipeline(ImagesPipeline):
    
    def get_media_requests(self, item, info):
            print('你来了没有啊')
            imageUrl = item["imageUrl"]
            realImageUrl = 'http://img.q6pk.com/image'+imageUrl
            return scrapy.Request(realImageUrl)

    def item_completed(self, results, item, info):
        image_path = [x["path"] for ok, x in results if ok]
        os.rename(images_store+image_path[0], images_store +item["name"])
        return item