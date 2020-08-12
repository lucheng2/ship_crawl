import scrapy
from scrapy import Selector

from ship.items import ShipSpiderItem
from scrapy.spiders.crawl import Rule, CrawlSpider
from scrapy.linkextractors import LinkExtractor
import sys
import re
import logging

from lxml import etree

keyword_to_item_k = {
    1: 'Name',
    2: 'Flag',
    3: 'MMSI',
    4: 'IMO',
    5: 'Call_Sign',
    6: 'Type',
    7: 'Size',
    8: 'Speed_AVG_or_MAX',
    9: 'Draught_AVG',
    10: 'GRT',
    11: 'DWT',
    12: 'Owner',
    13: 'Build'
}


class MySpider(CrawlSpider):
    """
    name:scrapy唯一定位实例的属性，必须唯一
    allowed_domains：允许爬取的域名列表，不设置表示允许爬取所有
    start_urls：起始爬取列表
    start_requests：它就是从start_urls中读取链接，然后使用make_requests_from_url生成Request，
                    这就意味我们可以在start_requests方法中根据我们自己的需求往start_urls中写入
                    我们自定义的规律的链接
    parse：回调函数，处理response并返回处理后的数据和需要跟进的url
    log：打印日志信息
    closed：关闭spider
    """
    # # 设置name
    name = "ship"
    # 设定域名
    # allowed_domains = ["www.myshiptracking.com"]
    # #     # 填写爬取地址
    # start_urls = [
    #     "https://www.myshiptracking.com/vessels"
    host = "https://www.myshiptracking.com"
    # # start_urls是我们准备爬的初始页
    start_urls = [
        'https://www.myshiptracking.com/vessels?page=' + str(i) for i in range(1, 31652)
    ]

    # # 1: 1~1501
    # start_urls = [
    #     'https://www.myshiptracking.com/vessels?page=' + str(i) for i in range(1, 1501)
    # ]

    # # 2: 1501~3001
    # start_urls = [
    #     'https://www.myshiptracking.com/vessels?page=' + str(i) for i in range(1501, 3001)
    # ]

    # # 3: 3001~4501
    # start_urls = [
    #     'https://www.myshiptracking.com/vessels?page=' + str(i) for i in range(3001, 4501)
    # ]

    # # 4: 4501~6001
    # start_urls = [
    #     'https://www.myshiptracking.com/vessels?page=' + str(i) for i in range(4501, 6001)
    # ]

    # # 5: 6001~7501
    # start_urls = [
    #     'https://www.myshiptracking.com/vessels?page=' + str(i) for i in range(6001, 7501)
    # ]

    # # 6: 7501~9001
    # start_urls = [
    #     'https://www.myshiptracking.com/vessels?page=' + str(i) for i in range(7501, 9001)
    # ]

    # # 7: 9001~10501
    # start_urls = [
    #     'https://www.myshiptracking.com/vessels?page=' + str(i) for i in range(9001, 10501)
    # ]

    # # 8: 10501~12001
    # start_urls = [
    #     'https://www.myshiptracking.com/vessels?page=' + str(i) for i in range(10501, 12001)
    # ]

    # # 9: 12001~13501
    # start_urls = [
    #     'https://www.myshiptracking.com/vessels?page=' + str(i) for i in range(12001, 13501)
    # ]

    # # 10: 13501~15001
    # start_urls = [
    #     'https://www.myshiptracking.com/vessels?page=' + str(i) for i in range(13501, 15001)
    # ]

    # # 11: 15001~16501
    # start_urls = [
    #     'https://www.myshiptracking.com/vessels?page=' + str(i) for i in range(15001, 16501)
    # ]

    # # 12: 16501~18001
    # start_urls = [
    #     'https://www.myshiptracking.com/vessels?page=' + str(i) for i in range(16501, 18001)
    # ]

    # # 13: 18001~19501
    # start_urls = [
    #     'https://www.myshiptracking.com/vessels?page=' + str(i) for i in range(18001, 19501)
    # ]

    # # 14: 19501~21001
    # start_urls = [
    #     'https://www.myshiptracking.com/vessels?page=' + str(i) for i in range(19501, 21001)
    # ]

    # # 15: 21001~22501
    # start_urls = [
    #     'https://www.myshiptracking.com/vessels?page=' + str(i) for i in range(21001, 22501)
    # ]

    # # 16: 22501~24001
    # start_urls = [
    #     'https://www.myshiptracking.com/vessels?page=' + str(i) for i in range(22501, 24001)
    # ]

    # # 17: 24001~25501
    # start_urls = [
    #     'https://www.myshiptracking.com/vessels?page=' + str(i) for i in range(24001, 25501)
    # ]

    # # 18: 25501~27001
    # start_urls = [
    #     'https://www.myshiptracking.com/vessels?page=' + str(i) for i in range(25501, 27001)
    # ]

    # # 19: 27001~28501
    # start_urls = [
    #     'https://www.myshiptracking.com/vessels?page=' + str(i) for i in range(27001, 28501)
    # ]

    # # 20: 28501~30001
    # start_urls = [
    #     'https://www.myshiptracking.com/vessels?page=' + str(i) for i in range(28501, 30001)
    # ]

    # # 21: 30001~31652
    # start_urls = [
    #     'https://www.myshiptracking.com/vessels?page=' + str(i) for i in range(30001, 31652)
    # ]

    def parse(self, response):
        selector = Selector(response)
        # 在此，xpath会将所有class=topic的标签提取出来，当然这是个list
        # 这个list里的每一个元素都是我们要找的html标签
        content_list = selector.xpath("//*[@class='dropdown-menu pull-right hist-menu-1']/li[2]/a")
        # 遍历这个list，处理每一个标签
        for content in content_list:
            # 此处提取出帖子的url地址。
            url = self.host + content.xpath('@href').extract_first()
            print("url:\n" + url)
            yield scrapy.Request(url, callback=self.parse_item, dont_filter=True)

    # def __init__(self, site, start_urls):
    #     re_rule = '[\w\W]*{}[\w\W]*'.format(site)
    #     rule = [Rule(LinkExtractor(allow=re_rule), callback='parse_item', follow=True)]
    #     CrawlSpider.__init__(self, allowed_domains=[site], start_urls=[start_urls], rules=rule)
    #     self.brands = KEYWORDS
    #     self.site = site
    #     logging.getLogger(__name__).debug("start site: {}".format(self.site[4:]))

    # 编写爬取方法
    def parse_item(self, response):
        # body = response.body.decode(response.encoding)
        item = ShipSpiderItem()
        for i in range(1, 14):
            item[keyword_to_item_k[i]] = response.xpath(
                '//table[@class="vessels_table"]//tr[' + str(i) + ']//td[2]//text()').extract()
            # print("item:\n" + str(item))
        yield item

# item[keyword_to_item_k[i]] = response.url
