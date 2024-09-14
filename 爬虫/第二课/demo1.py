#爬虫基础 requests
import requests
res = requests.get()#明文请求
res = requests.post()#密文请求
#状态码 2开头ok    4访问失败  5开头服务器内部错误

#text获取文本，网页源代码
#content获取二进制内容：视频、音乐、图片、文件
#json()获取网页格式的字典、列表（json） 
