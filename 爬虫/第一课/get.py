#导库 基础爬虫 requests
import requests

#寻址 目标网址
url = "https://www.baidu.com/s?wd=ai"

#请求，get请求传的是明文参数
res = requests.get(url)

#处理数据
print(res)