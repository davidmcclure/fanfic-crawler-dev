

from scrapy import Spider

from fanfic.items import BookMetadataItem


class BookMetadataSpider(Spider):

    name = 'book_metadata'

    start_urls = ['https://www.fanfiction.net/s/11007271']

    def parse(self, res):

        """
        Pull out book metadata fields.

        Args:
            res (scrapy.Response)
        """

        title = (
            res.selector
            .xpath('//div[@id="profile_top"]/b/text()')
            .extract_first()
        )

        username = (
            res.selector
            .xpath('//div[@id="profile_top"]/a/text()')
            .extract_first()
        )

        summary = (
            res.selector
            .xpath('//div[@id="profile_top"]/div/text()')
            .extract_first()
        )

        metadata = (
            res.selector
            .xpath('//div[@id="profile_top"]/span[position() = last()]//text()')
            .extract()
        )

        metadata = ''.join(metadata)

        metadata_parts = metadata.split('-')

        labels = {}
        for part in metadata_parts:

            part = part.strip()

            if ':' in part:
                label, value = part.split(':')
                labels[label.strip()] = value.strip()

            elif '/' in part:
                labels['Genres'] = part

            elif part != 'English':
                labels['Characters'] = part

        yield BookMetadataItem(
            title=title,
            username=username,
            summary=summary,
            rated=labels['Rated'],
            genres=labels['Genres'],
            characters=labels['Characters'],
            favs=int(labels['Favs']),
            follows=int(labels['Follows']),
            published=labels['Published'],
        )

        print(summary)
