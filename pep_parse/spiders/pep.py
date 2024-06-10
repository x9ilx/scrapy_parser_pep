import scrapy

from pep_parse.items import PepParseItem


class PepSpider(scrapy.Spider):
    name = 'pep'
    allowed_domains = ['peps.python.org']
    start_urls = ['https://peps.python.org/']

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
