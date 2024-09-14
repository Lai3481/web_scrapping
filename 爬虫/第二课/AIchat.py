#http://api.qingyunke.com/
#导库
import requests

while True:
    #寻址
    url = "http://api.qingyunke.com/api.php?key=free&appid=0&msg="
    x = input("你说：")
    #访问
    res = requests.get(url+x)

    #处理数据
    res2 = res.json()  #把json格式转化为python字典格式
    print("菲菲说：",res2["content"])
