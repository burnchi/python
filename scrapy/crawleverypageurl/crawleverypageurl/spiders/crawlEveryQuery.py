import scrapy
import re


class CrawleveryquerySpider(scrapy.Spider):
    name = "Crawleveryquery"
    allowed_domains = ["uukanshu.net"]
    start_urls = ["https://www.uukanshu.net/list/xuanhuan-1.html#gsc.tab=0",
                  "https://www.uukanshu.net/list/yanqing-1.html#gsc.tab=0",
                  "https://www.uukanshu.net/list/xianxia-1.html",
                  "https://www.uukanshu.net/list/lishi-1.html#gsc.tab=0",
                  "https://www.uukanshu.net/list/wangyou-1.html#gsc.tab=0",
                  "https://www.uukanshu.net/list/lingyi-1.html#gsc.tab=0",
                  "https://www.uukanshu.net/list/tongren-1.html#gsc.tab=0",
                  "https://www.uukanshu.net/list/erciyuan-1.html#gsc.tab=0",
                  ]

    def parse(self, response):

        yield {
            "url_query": response.url
        }
        # next page
        next_page_url = response.xpath(
            "//div[@class='page']/a[contains(text(), '下一页')]/@href").get()
        if next_page_url is not None:
            yield response.follow(next_page_url, callback=self.parse)
