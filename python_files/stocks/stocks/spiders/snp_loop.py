import scrapy
from spiders.items import StocksItem


class SnpLoopSpider(scrapy.Spider):
    name = "snp_loop"
    allowed_domains = ["en.wikipedia.com"]
    start_urls = ["https://en.wikipedia.org/wiki/List_of_S%26P_500_companies"]

    def parse(self, response):
        rows = response.xpath('//*[@id="contituents"]/tbody/tr')
        for rows in self:

        symbol = response.xpath('//table[@id="constituents"]//td[1]/a/text()').get()
        security = response.xpath('//table[@id="constituents"]//td[2]/a/text()').get()
        sector = response.xpath('//table[@id="constituents"]//td[3]/text()').get()
        hq = response.xpath('//table[@id="constituents"]//td[5]/a/text()').get()
        date = response.xpath('//table[@id="constituents"]//td[6]/text()').get()

        return {"symbol" : symbol, "security": security, "sector" : sector,
                 "hq" : hq, "date" : date}
