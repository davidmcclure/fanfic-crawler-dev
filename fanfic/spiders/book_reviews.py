

import re

from scrapy import Spider, Request

from fanfic.items import BookReviewItem


class BookReviewsSpider(Spider):

    name = 'book_reviews'

    start_urls = ['https://www.fanfiction.net/r/11863209/']

    def parse(self, res):

        """
        Extract comments, go next page.

        Args:
            res (scrapy.Response)
        """

        for tr in res.selector.xpath('//table[@id="gui_table1i"]/tbody/tr'):

            username = tr.xpath('.//a[position() = last()]/text()').extract_first()

            small = tr.xpath('.//small//text()').extract()

            chapter = ''.join(small).split('.')[0]

            chapter_number = int(re.search('[0-9]+', chapter).group(0))

            xutime = tr.xpath('.//span/@data-xutime').extract_first()

            content = tr.xpath('.//div/text()').extract_first()

            yield BookReviewItem(
                username=username,
                chapter=chapter_number,
                timestamp=xutime,
                content=content,
            )

        next_href = res.selector.xpath('//a[text()="Next »"]/@href').extract_first()

        next_url = res.urljoin(next_href)

        yield Request(next_url)
