from bs4 import BeautifulSoup
import requests

url = "https://www.thepaper.cn/newsDetail_forward_26425054"

res = requests.get(url)

#处理数据阶段使用bs4   BeautifulSoup(网页源代码,解析器)
bs = BeautifulSoup(res.text, "html.parser")  #返回解析后的一个内容对象

#解析后的内容对象包含很多查询方法，获取数据的方法

#查找所有满足条件的标签，返回的是列表  find_all(标签名,属性值)
units = bs.find_all("div",class_ = "index_cententWrap__Jv8jK")

# for i in units:
#     print(i.text)

#select查找所有满足选择器的标签，返回一个列表  select(选择器)
units2 = bs.select(".index_cententWrap__Jv8jK")
for i in units2:
    print(i.text)