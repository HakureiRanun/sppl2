import scrapy
from scrapy import Request
from tutorial.items import SpplItem
import logging
import time
import requests
from git import Repo
import os
class MinoriSpider(scrapy.spiders.Spider):
    name = "minori"
    allowed_domains = ["http://www.mangagamer.org/"]
    start_urls = [
        "http://www.mangagamer.org/minori/",
    ]

    def parse(self, response):
        sppl = SpplItem()
        sppl["Date"] = time.strftime('%Y-%m-%d',time.localtime())
        sppl["price"] = response.xpath('//span[@class="current"]/text()').extract()[0]
        with open('sppl.json','ab') as f:
            f.write(","+str(sppl))
        yield sppl