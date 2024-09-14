#导库
#http://tianqiapi.com/index
import requests
while True:
    city = input("请输入城市：")
    #寻址
    url = "http://v1.yiketianqi.com/api?appid=52337255&appsecret=D6sbQoqu&city="+city
    #请求
    res = requests.get(url)
    #处理数据
    res2 = res.json()#获取的数据会转化为python字典
    print(res2["city"])
    data = res2["data"][0]#只要列表中第一日的天气数据
    print("天气是：",data["wea"])
    print("温度是：",data["tem"])
    print("湿度是：",data["humidity"])