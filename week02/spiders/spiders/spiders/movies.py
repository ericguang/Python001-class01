import scrapy
from spiders.items import SpidersItem 


class MoviesSpider(scrapy.Spider):
    name = 'movie'
    allowed_domains = ['maoyan.com']
    start_urls = ['https://maoyan.com/films?showType=3']

    def parse(self, response):
        # pass
        items = []
        i = 0
        for each in response.xpath('//div[@class="movie-hover-info"]'):
            if (i < 10):
                item = SpidersItem()
                title = each.xpath('div[2]/@title').extract_first().strip()
                category = each.xpath('div[2]/text()[2]').extract_first().strip()
                date = each.xpath('div[4]/text()[2]').extract_first().strip()

                item['title'] = title
                item['category'] = category
                item['date'] = date
                print("============================================")
                print(item)
                items.append(item)
                i += 1
            # yield item
            # print(items) settings.py 中pipeline需要打开
        return items   
        #return items 是传递给pipline 