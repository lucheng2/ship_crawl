# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import json

from itemadapter import ItemAdapter


class FilePipeline:
    def process_item(self, item, spider):
        with open("./ship_info.json", "w", encoding='utf-8') as f:
            content = json.dumps(dict(item), ensure_ascii=False) + "\n"
            f.write(content)

