# -*- coding: utf-8 -*-
import scrapy
import urllib
import time
__author__ = 'du_du'


class QSpider(scrapy.Spider):
    # 爬虫的名字
    name = "Lilian"
    # 允许爬取得范围
    allowed_domains = [
        "https://www.qiushibaike.com/"
    ]
    start_urls = [
        "https://qiushibaike.com/pic/"
    ]

    # 接受返回数据的方法
    def parse(self, response):
        xpath_list = response.epath("//img")
        for x in xpath_list:
            src = x.xpath("@scr")[0].extract()  # 获取具体的内容
            scr = "http:" + scr
            if "?" in scr:
                path = scr.split("?", 1)[0]
            else:
                path = src
            file_name = path.rstrip("/", 1)[1]
            file_path = r"D:\\Cache\\Box"
            file_name = file_path + "\\" + file_name
            try:
                urllib.urlretrieve(src, file_name)
                time.sleep(1)
            except Exception as e:
                self.log(str(e))

