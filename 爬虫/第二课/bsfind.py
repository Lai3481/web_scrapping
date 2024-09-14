from bs4 import BeautifulSoup
import requests

url = "https://www.thepaper.cn/newsDetail_forward_26425054"

res = requests.get(url)

#处理数据阶段使用bs4   BeautifulSoup(网页源代码,解析器)
bs = BeautifulSoup(res.text, "html.parser")  #返回解析后的一个内容对象

#解析后的内容对象包含很多查询方法，获取数据的方法

#单独查找  使用bs对象的find方法  find(标签名, 属性值)

unit = bs.find("div",class_ = "index_cententWrap__Jv8jK")

# 查询子标签
image = unit.img

#beutifulsoup自动将所有属性与属性值转化为一个字典
# print(image.attrs) #该标签所有属性的字典

url2 = image.attrs["src"]

res = requests.get(url2)

with open("image.png","wb") as f:
    f.write(res.content)
