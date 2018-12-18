# -*- coding: utf-8 -*-
import scrapy
from scrapy.mail import MailSender

class RadomspiderSpider(scrapy.Spider):
    name = 'radomspider'
    allowed_domains = ['douban.com']
    start_urls = ['http://baidu.com/']

    def parse(self, response):
        print("====="*50)
        print(response.request.headers['User-Agent'])
        print("=====" * 50)
        # yield scrapy.Request(self.start_urls[0], dont_filter=True)

    def closed(self, reason):  # 爬取结束的时候发送邮件
        mailer = MailSender(
            smtphost="smtp.163.com",  # 发送邮件的服务器
            mailfrom="wumiaosheng08@163.com",  # 邮件发送者
            smtpuser="wumiaosheng08@163.com",  # 用户名
            smtppass="123456miaosheng",  # 发送邮箱的密码不是你注册时的密码，而是授权码！！！切记！
            smtpport=25  # 端口号
        )
        body = u"测试发送---"
        subject = u'测试发送---标题'
        # 如果说发送的内容太过简单的话，很可能会被当做垃圾邮件给禁止发送。
        mailer.send(to=["515824031@qq.com", "515824031@qq.com"], subject=subject, body=body)
