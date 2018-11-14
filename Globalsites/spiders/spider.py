# -*- coding: utf-8 -*-
import scrapy
# import domainName_config

from scrapy.spiders import CrawlSpider
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor


class GlobalsitesSpider(CrawlSpider):
    name = 'globalWebsiteSites'
    allowed_domains = [input('in format www.capitalfm.com: ')]

    start_urls = [input('in format http://www.capitalfm.com: ')]


    rules = [

        #Rule(LinkExtractor(allow=[r'/radio/\w*'], deny=[r'/?redirect_url=/\w*']),
        Rule(LinkExtractor(deny=[r'/?redirect_url=/\w*']),
        callback='parse_item',
        follow = True)

    ]


    def parse_item(self, response):
        print(response.url)
        for title in response.css('title'):
            yield {
                    'url': response.url,
                    'title of page': title.css('title::text').extract_first(),
                    'MPU adid': title.xpath('//div[@class="dac__mpu"]').extract_first(),
                    'Instream adid': title.xpath('//div[@class="dac__instream"]').extract_first(),
                    'Banner adid': title.xpath('//div[@class="dac__banner"]').extract_first(),
                    'Overlay adid': title.xpath('//div[@class="dac__overlay"]').extract_first(),

            }
