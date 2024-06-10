import scrapy

from pep_parse.items import PepParseItem
from pep_parse.settings import (PEP_SPIDER_ALLOWED_HOST, PEP_SPIDER_NAME,
                                PEP_SPIDER_START_URL)


class PepSpider(scrapy.Spider):
    name = PEP_SPIDER_NAME
    allowed_domains = [
        PEP_SPIDER_ALLOWED_HOST,
    ]
    start_urls = [
        PEP_SPIDER_START_URL,
    ]

    def parse(self, response):
        for pep_line in response.css('section[id="numerical-index"] tbody tr'):
            pep_link = pep_line.css('a::attr(href)').get()
            yield response.follow(pep_link, callback=self.parse_pep)

    def parse_pep(self, response):
        pep_info = response.css('dl.field-list')
        status = pep_info.xpath(
            '//dt[text()="Status"]/following-sibling::dd/abbr/text()'
        ).get()
        pep_header = response.css('h1.page-title::text').get()
        pep_header_split = pep_header.split(' – ')
        pep_name = pep_header_split[1]
        pep_number = int(pep_header_split[0].split()[1])

        yield PepParseItem(
            {
                'number': pep_number,
                'name': pep_name,
                'status': status,
            }
        )
