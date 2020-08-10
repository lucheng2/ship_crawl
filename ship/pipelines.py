# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import json


class FilePipeline:
    def process_item(self, item, spider):
        with open("./ship_info.json", "a+", encoding='utf-8') as f:
            content = json.dumps(dict(item), ensure_ascii=False) + "\n"
            f.write(content)

        # # 字典中的key值即为csv中列名
        # dataframe = pd.DataFrame(item)
        # # 将DataFrame存储为csv,index表示是否显示行名，default=True
        # dataframe.to_csv("ship_info.csv", index=False, sep=',')

