# 安装依赖包
- pip install -r requirement.txt

# 选择爬取的页面
- 在spiders/myspider.py里面选择合适的页面

# 开始爬取
- scrapy crawl ship

# json 转 csv
- python ship/json2csv.py json文件路径

# prox_list.txt里面是ip代理池的地址, 主要来源网站如下(按爬取速度排序):
- https://www.proxy-list.download/HTTP
- https://github.com/clarketm/proxy-list
- https://www.proxyscan.io/

# 合并多个json文件的工具
- python merge_files.py json文件所在的目录 目标json文件



