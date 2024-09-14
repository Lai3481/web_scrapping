#进阶爬虫

import requests
res = requests.get("https://www.thepaper.cn/newsDetail_forward_26425054")

print(res.text)