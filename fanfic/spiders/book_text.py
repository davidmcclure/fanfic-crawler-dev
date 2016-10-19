

import re

from scrapy import Spider, Request

class BookTextSpider(Spider):

    name = 'book_text'

    start_urls = ['https://www.fanfiction.net/s/11762850']

    def parse(self, res):

        """
        Pull out the chapter text, go to next page.

        Args:
            res (scrapy.Response)
        """

        text = res.selector.xpath('//div[@id="storytextp"]').extract_first()

        next_onclick = res.selector.xpath('//button[text()="Next >"]/@onclick').extract_first()

        next_href = re.search('\'(?P<url>.*)\'', next_onclick).group('url')

        next_url = res.urljoin(next_href)

        yield Request(next_url)
