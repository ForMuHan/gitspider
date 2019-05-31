# -*- coding: utf-8 -*-
import scrapy
from gitspider.items import GitspiderItem


class ItcastSpider(scrapy.Spider):
    name = "qiushibaike"
    allowed_domains = ["qiushibaike.com"]

    # 设置start_urls
    url = "https://www.qiushibaike.com/text/page/"
    offset = 1
    start_urls = [url + str(offset)]

    def parse(self, response):
        for each in response.xpath("//div[contains(@id,'qiushi_tag')]"):
            # 初始化模型对象
            item = GitspiderItem()
            # xpath解析出来为列表
            # scrapy中xpath解析出来的类型为 scrapy里边的Selector类型，需要用extract（）提取出来。
            if (len(each.xpath(".//div/a/h2/text()")) == 0):
                item['positionname'] = '匿名用户'
            else:
                item['positionname'] = each.xpath(".//div/a/h2/text()").extract()[0]

            # 解析段子内容
            item['positionmsg'] = each.xpath(".//a/div/span//text()").extract()

            # 将每一条数据提交给pipelins文件处理
            yield item

        if self.offset < 13:
            self.offset += 1

            # 每次处理完一页的数据之后，重新发送下一页页面请求
            # self.offset自增1，同时拼接为新的url，并调用回调函数self.parse处理Response
            yield scrapy.Request(self.url + str(self.offset), callback=self.parse)
