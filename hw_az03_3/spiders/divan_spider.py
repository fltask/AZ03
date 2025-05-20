import scrapy

class DivanSpiderSpider(scrapy.Spider):
    name = "divan_spider"
    allowed_domains = ["divan.ru"]
    # чтобы ловить любые статусы, не только 200
    handle_httpstatus_list = list(range(400, 600))

    def start_requests(self):
        url = "https://www.divan.ru/category/divany-i-kresla"
        yield scrapy.Request(url, callback=self.parse, meta={'page': 1})

    def parse(self, response):
        page = response.meta['page']

        # прекращаем, если ответ не успешен (не в 200–299)
        if not (200 <= response.status < 300):
            self.logger.info(f"Страница {page} вернула статус {response.status}. Останавливаемся.")
            return

        divans = response.css('div._Ud0k')
        if not divans:
            self.logger.info(f"На странице {page} нет товаров. Останавливаемся.")
            return

        for divan in divans:
            yield {
                'name':  divan.css('div.lsooF span::text').get(),
                'price': divan.css('div.pY3d2 span.ui-LD-ZU::text').get(),
                'url':   response.urljoin(divan.css('div.lsooF a::attr(href)').get()),
                'page':  page,
            }

        next_url = f"https://www.divan.ru/category/divany-i-kresla/page-{page+1}"
        yield scrapy.Request(
            next_url,
            callback=self.parse,
            meta={'page': page+1},
            dont_filter=True
        )
