import scrapy

class LightingSpider(scrapy.Spider):
    name = "lighting"
    allowed_domains = ["https://www.divan.ru"]
    start_urls = ["https://www.divan.ru/category/svet"]

    def parse(self, response):
        lightings = response.css('div._Ud0k')
        for lighting in lightings:
            yield {
                'name': lighting.css('div.lsooF span::text').get(),
                'price': lighting.css('div.pY3d2 span::text').get(),
                'url': response.urljoin(lighting.css('a').attrib['href'])
            }

