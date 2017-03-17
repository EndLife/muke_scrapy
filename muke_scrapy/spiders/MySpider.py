# coding:utf-8
# 
import scrapy
from scrapytest.CourseItems import CourseItem

class MySpider(scrapy.Spider):

    name = "MySpider"
    allowed_domains = ["imooc.com"]
    start_urls = ["http://www.imooc.com/course/list"]
    # 爬取方法
    def parse(self, response):
        item = CourseItem()
        # xpath
        for box in response.xpath('//div[@class="moco-course-wrap"]/a[@target="_self"]'):
            #课程路径
            item['url'] = 'http://www.imooc.com' + box.xpath('.//@href').extract()[0]
            #课程标题
            item['title'] = box.xpath('.//img/@alt').extract()[0].strip()
            #标题图片地址
            item['image_url'] = box.xpath('.//@src').extract()[0]
            #学生人数
            item['student'] = box.xpath('.//span/text()').extract()[0].strip()[:-3]
            #课程简介
            item['introduction'] = box.xpath('.//p/text()').extract()[0].strip()
            #返回信息
            yield item
        #url跟进开始
        #获取下一页的url信息
        url = response.xpath("//a[contains(text(),'下一页')]/@href").extract()
        if url :
            #将信息组合成下一页的url
            page = 'http://www.imooc.com' + url[0]
            #返回url
            yield scrapy.Request(page, callback=self.parse)
        #url跟进结束
