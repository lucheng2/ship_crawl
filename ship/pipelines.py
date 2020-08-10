# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import json
from datetime import datetime

from pydispatch import dispatcher
from scrapy import signals


class FilePipeline:

    def __init__(self):
        dispatcher.connect(self.spider_opened, signal=signals.spider_opened)
        dispatcher.connect(self.spider_closed, signal=signals.spider_closed)

    def process_item(self, item, spider):
        with open("./ship_info.json", "a+", encoding='utf-8') as f:
            content = json.dumps(dict(item), ensure_ascii=False) + "\n"
            f.write(content)

    def spider_opened(self, spider):
        spider.started_on = datetime.now()
        print(spider.started_on)

    def spider_closed(self, spider):
        spider.work_time = datetime.now() - spider.started_on
        print("total time: " + str(spider.work_time))

# # 字典中的key值即为csv中列名
# dataframe = pd.DataFrame(item)
# # 将DataFrame存储为csv,index表示是否显示行名，default=True
# dataframe.to_csv("ship_info.csv", index=False, sep=',')
