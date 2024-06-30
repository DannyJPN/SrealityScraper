import scrapy


class SrealitycrawlerSpider(scrapy.Spider):
    name = "srealitycrawler"
    allowed_domains = ["sreality.cz"]
    start_urls = ["https://sreality.cz"]

    def parse(self, response):
        pass
