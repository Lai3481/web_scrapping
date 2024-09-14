#导库
import requests
from bs4 import BeautifulSoup
import time

#寻址
url ="https://www.qidian.com/book/114559/"

#伪装身份，添加headers
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Language': 'en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7',
    'Accept-Encoding': 'gzip, deflate, br',
    'DNT': "1",
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',
    'Sec-Fetch-Site': 'none',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-User': '?1',
    'Sec-Fetch-Dest': 'document',
    'Cookie':'_yep_uuid=602e6195-a999-195b-c267-885b3fddc5b5; e2=%7B%22l6%22%3A%221%22%2C%22l1%22%3A%22%22%2C%22pid%22%3A%22qd_P_xiangqing%22%2C%22eid%22%3A%22%22%7D; e1=%7B%22l6%22%3A%221%22%2C%22l1%22%3A2%2C%22pid%22%3A%22qd_P_xiangqing%22%2C%22eid%22%3A%22%22%7D; newstatisticUUID=1710485666_1802557666; _csrfToken=ljNtl4r44pWWEKODIrcsgnApfeGCAq4xEL0cv2Gr; fu=1877307984; traffic_utm_referer=; _gid=GA1.2.1339482135.1710485669; supportwebp=true; supportWebp=true; trkf=1; Hm_lvt_f00f67093ce2f38f215010b699629083=1710485668,1710502376; _yep_uuid=44f0ace1-c8a2-9442-48b7-d2a40af16d07; e1=%7B%22l6%22%3A%22%22%2C%22l1%22%3A3%2C%22pid%22%3A%22qd_p_qidian%22%2C%22eid%22%3A%22qd_A18%22%7D; e2=%7B%22l6%22%3A%22%22%2C%22l1%22%3A9%2C%22pid%22%3A%22qd_p_qidian%22%2C%22eid%22%3A%22%22%2C%22l2%22%3A1%7D; Hm_lpvt_f00f67093ce2f38f215010b699629083=1710503039; _ga_FZMMH98S83=GS1.1.1710502376.3.1.1710503038.0.0.0; _ga=GA1.1.863536092.1710485668; _ga_PFYW0QLV3P=GS1.1.1710502376.3.1.1710503038.0.0.0; w_tsfp=ltvgWVEE2utBvS0Q6KrtnE6oED07Z2R7xFw0D+M9Os09AKYhUZuG04ByutfldCyCt5Mxutrd9MVxYnGBU9YmeBIXQ8SRb5tH1VPHx8NlntdKRQJtA5rfUVIZKr0h5DkSdTxXI0PljDx+IYVDxOdhi1kF5yF837ZlCa8hbMFbixsAqOPFm/97DxvSliPXAHGHM3wLc+6C6rgv8LlSgW2DugDuLi11A7hB1kCR0C0XG3pV8w2pJbsDal7wcpK9Uv8wrTPzwjn3apCs2RYj4VA3sB49AtX02TXKL3ZEIAtrZUqukO18Lv3wdaN4qzsLDqgaGwwWqlwd4eo7qhJJDn3sZ3OOVPtzvQFVRqZfrcq+NA==',
}

res = requests.get(url,headers=headers)


#处理数据阶段
#只要网页部分内容==》BeautifulSoup

bs = BeautifulSoup(res.text, "html.parser")

bs_a = bs.find_all("a",class_="chapter-name")

for a in bs_a:
    id = a["href"].split("/")[-2]
    name = a.text
    if "第" in name:
        new_url = f"https://www.qidian.com/chapter/114559/{id}/"
        new_res = requests.get(url= new_url, headers=headers)
        new_soup = BeautifulSoup(new_res.text, "html.parser")
        new_html_p = new_soup.find_all("p")
        #open的模式  w wb r rb a 
        with open("2.txt", mode="a",encoding="utf-8") as f:
            for i in new_html_p:
                f.write(i.text+"\n\n")
