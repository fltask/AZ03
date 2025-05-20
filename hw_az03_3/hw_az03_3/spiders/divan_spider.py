import scrapy


class DivanSpiderSpider(scrapy.Spider):
    name = "divan_spider"
    allowed_domains = ["divan.ru"]
    start_urls = ["https://divan.ru"]

    def parse(self, response):
        pass
