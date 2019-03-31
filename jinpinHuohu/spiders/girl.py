# -*- coding: utf-8 -*-
import scrapy
import json
from jinpinHuohu.items import JinpinhuohuItem

class GirlSpider(scrapy.Spider):
    name = 'girl'
    allowed_domains = ['api12.tubaxian.com', 'api12.tubaxian.com']
    index = 1;
    listbaseurl = 'http://api12.tubaxian.com/api/content/contentList?cat_id=0&sort=0&type=2&page='
    detailbaseurl = 'http://api12.tubaxian.com/api/content/nextImageInfo?c_id='
    start_urls = [listbaseurl + str(index)]

    def parse(self, response):
        girl_data = json.loads(response.body)['data']['info_list']
        if len(girl_data) != 0:
            otherDic = girl_data[0]
            if 'content' in otherDic:
                for girDic in girl_data:
                    for temurl in girDic['content']:
                        item = JinpinhuohuItem()
                        item['imageUrl'] = temurl
                        # print(temurl)
                        name = temurl.split('/')[-1]
                        item['name'] = name
                        # print(name)
                        yield item
            else:
                for dic in girl_data:
                    c_id = dic['id']
                    url = self.detailbaseurl + str(c_id)
                    print(url)
                    yield scrapy.Request(url, callback=self.parse)
        

        
           

        if len(girl_data) != 0:
            self.index += 1
            yield scrapy.Request(self.listbaseurl + str(self.index), callback=self.parse)
        
