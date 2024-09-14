#导库
import requests
from bs4 import BeautifulSoup
import time

#寻址
url = "https://www.bg60.cc/book/72268/"

#请求
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36'
}

res = requests.get(url, headers=headers)

#处理数据
bs = BeautifulSoup(res.text, "html.parser")

soup_html = bs.select("div.listmain dl dd a")#逐次查找，找到需要的a标签，select返回一个列表

for html in soup_html:
    href = html["href"]  #获取每个章节的超链接
    name = html.text
    if "/book" in href:  #筛选超链接
        new_url = f"https://www.bg60.cc{href}"
        new_res = requests.get(new_url,headers=headers)
        new_soup = BeautifulSoup(new_res.text, "html.parser")
        div_id = new_soup.find("div",id="chaptercontent")
        with open(f"txt/{name}.txt",mode="a",encoding="utf-8") as f:
            print(f"正在下载：《{name}》，请稍后~")
            f.write(div_id.text+"\n\n")
            time.sleep(1)