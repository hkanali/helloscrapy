# -*- coding: utf-8 -*-

from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from scrapy.http.request import Request
from helloscrapy.items import FirstProjItem

class FooSpider(BaseSpider):
    name = "foo"
    allowed_domains = ["foo.org"]
    start_urls = ["https://twitter.com/nhk_pr"]

    def parse(self, response):
        hxs = HtmlXPathSelector(response)

        sites = hxs.select("//*/div/div[2]")
        items = []        #for post in posts:
        for site in sites:
            item = FirstProjItem()
            item["title"] = site.select('p/text()').extract()
            item["link"] = site.select('a/@href').extract()
            item["content"] = site.select('text()').extract()
            items.append(item)
        for item in items:
            yield item
