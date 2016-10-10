

from scrapy import Spider, Request

from fanfic.items import BookIdItem


class BookIdsSpider(Spider):

    name = 'book_ids'

    start_urls = ['https://www.fanfiction.net/book/Harry-Potter/?&srt=2&lan=1&r=10&len=60&p=2']

    def parse(self, res):

        """
        Extract book titles, generate book ids.

        Args:
            res (scrapy.Response)
        """

        for href in res.selector.xpath('//a[@class="stitle"]/@href').extract():
            book_id = href.split('/')[2]
            yield BookIdItem(book_id=book_id)

        next_href = res.selector.xpath('//a[text()="Next »"]/@href').extract_first()

        next_url = res.urljoin(next_href)

        yield Request(next_url)
