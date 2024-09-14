#导库
import requests

#目标网址
url = "http://httpbin.org/post"

#设置post参数
abc = {"wd":"python","mima":"abcABC123!"}

#post请求传的是密文参数
res = requests.post(url,data=abc)

#处理数据
print(res)