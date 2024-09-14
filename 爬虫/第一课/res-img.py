#导库
import requests

#寻址
url = "https://www.baidu.com/img/PCtm_d9c8750bed0b3c7d089fa7d55720d6cf.png"

#请求
res = requests.get(url)

#处理数据
# print(res.status_code)  #状态码

# print(res.headers)#查看寄件人身份信息

# print(res.text)

#视频、音乐、图片、文件都用content属性获取
#文本、源代码用text属性获取
#网页的字典类型json类型，用json()获取

with open("image2.png","wb") as f:
    f.write(res.content)
