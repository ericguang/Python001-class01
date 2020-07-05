# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymysql
from spiders import mysql_do 


class SpidersPipeline:
    def process_item(self, item, spider):
        
        # with open('maoyan_top10.csv', 'a+', encoding='utf_8_sig') as file:
        #     line = "{title},{category},{date}\n".format(
        #         title=item['title'],
        #         category=item['category'],
        #         date=item['date'])
        #     file.write(line)
        mysql_do.insert_movie(item['title'], item['category'], item['date'])
        return item
