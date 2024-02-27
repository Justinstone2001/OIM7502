import scrapy


class PerformanceSpider(scrapy.Spider):
    name = "performance"
    allowed_domains = ["slickcharts.com"]
    start_urls = ["http://slickcharts.com/sp500/performance"]

    def parse(self, response):
        for row in response.xpath('//table[@class="table table-hover table-borderless table-sm"]/tbody/tr'):
            yield {
                'number': row.xpath('td[1]/text()').get(),
                'company': row.xpath('td[2]/a/text()').get(),
                'symbol': row.xpath('td[3]/text()').get(),
                'ytd_return': row.xpath('td[6]/text()').get(),
            }
            
    