

from scrapy import Spider

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

            # TODO: Handle "Guest" users.

            username = tr.xpath('.//a[position() = last()]/text()')

            small = tr.xpath('.//small//text()').extract()

            chapter, date = ''.join(small).split('.')

            xutime = tr.xpath('.//span/@data-xutime').extract_first()

            print(xutime)
