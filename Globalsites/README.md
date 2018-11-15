Some problems may occur when installing onto ec2 and scrapy. Use the following command first to install scrapy on virtual env:
sudo yum install gcc libffi-devel python-devel openssl-devel
pip install Scrapy

Scrapy web spider to crawl a website and pull out any DIV containers, + page title. 

spider.py included the config
This has been setup to look for class ids on the page:

'url': response.url,
'title of page': title.css('title::text').extract_first(),
'MPU adid': title.xpath('//div[@class="dac__mpu"]').extract_first(),
'Instream adid': title.xpath('//div[@class="dac__instream"]').extract_first(),
'Banner adid': title.xpath('//div[@class="dac__banner"]').extract_first(),
'Overlay adid': title.xpath('//div[@class="dac__overlay"]').extract_first(),

domain urls and start url is setup as an input


Commands to use:
scrapy crawl globalWebsiteSites -o outputfile.json
scrapy crawl globalWebsiteSites -o outputfile.csv
