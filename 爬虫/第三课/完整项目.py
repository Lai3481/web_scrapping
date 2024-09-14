#项目：百度招聘爬虫系统

#项目总体思路：
#寻找json接口
#打开开发者工具进行调试，找到json接口（不断请求）
#解析json接口
#请求json接口
#处理数据
#保存数据（pandas）
import requests
from bs4 import BeautifulSoup
import time
import json  #把字符串转化为python
import pandas as pd

#json接口
url = "https://yiqifu.baidu.com/g/aqc/joblist/getDataAjax?"

headers = {
    'Accept':'application/json, text/plain, */*',
    'Accept-Encoding':'gzip, deflate, br, zstd',
    'Accept-Language':'zh-CN,zh;q=0.9',
    'Connection':'keep-alive',
    'Host':'yiqifu.baidu.com',
    'Referer':'https://yiqifu.baidu.com/g/aqc/joblist?q=python',
    'Sec-Ch-Ua':'"Chromium";v="122", "Not(A:Brand";v="24", "Google Chrome";v="122"',
    'Sec-Ch-Ua-Mobile':'?0',
    'Sec-Ch-Ua-Platform':'"Windows"',
    'Sec-Fetch-Dest':'empty',
    'Sec-Fetch-Mode':'cors',
    'Sec-Fetch-Site':'same-origin',
    'X-Requested-With':'XMLHttpRequest',
    'Cookie':'BIDUPSID=FFE582BA7343E4BDE8F2B0969587933A; PSTM=1701944630; BAIDUID=FFE582BA7343E4BDDB41B7BF2E661BA5:FG=1; BDUSS=NrUG9jTlVkRFBXa3V0bW5pNjNFUGdHaTdnc21rdXpkZUpvTU9nbFpaaGpVZEJsSVFBQUFBJCQAAAAAAAAAAAEAAABJQjjR0-nA1mNhcmV5eQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGPEqGVjxKhlc0; BDUSS_BFESS=NrUG9jTlVkRFBXa3V0bW5pNjNFUGdHaTdnc21rdXpkZUpvTU9nbFpaaGpVZEJsSVFBQUFBJCQAAAAAAAAAAAEAAABJQjjR0-nA1mNhcmV5eQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGPEqGVjxKhlc0; MCITY=-75%3A; H_WISE_SIDS_BFESS=40045_40166_40202_39662_40210_40216_40222; H_WISE_SIDS=39662_40210_40216_40222_40271_40294_40291_40289_40286_40317_40079; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; H_PS_PSSID=39662_40210_40216_40222_40271_40294_40291_40289_40286_40317_40079_40364_40352_40301_40381_40366; BA_HECTOR=81ak8h048gak8ga1a485a1849i0vgo1iuja9s1t; ZFY=SJTaRNG4jPGf5XpXAboM31VLOh8ATplB5TW1u:Atu7Tk:C; BAIDUID_BFESS=FFE582BA7343E4BDDB41B7BF2E661BA5:FG=1; BDRCVFR[feWj1Vr5u3D]=I67x6TjHwwYf0; delPer=0; PSINO=7; clue_site=pc; clue_ext=%7B%22referer%22%3A%22www.baidu.com%22%2C%22ref_eqid%22%3A%22b9d3408400103e780000000665e9c22e%22%7D; log_guid=9c965543f29ee6e76083129d371aaa8a; log_first_time=1709818419524; Hm_lvt_37e1bd75d9c0b74f7b4a8ba07566c281=1709818420; Hm_lpvt_37e1bd75d9c0b74f7b4a8ba07566c281=1709818903; log_last_time=1709818910917',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36'
}

#发送请求
def send_get(page):
    try:  #捕捉错误，查看是否有错误
        params = f"q=python&page={page}&pagesize=20&district=110000&salaryrange="
        res = requests.get(url, headers = headers, params=params)
        res_loads = res.json()#转化json为字典
        res_list = res_loads["data"]["list"]#索引出装满职位的列表
        return res_list
    except:  #如果以上代码发生错误，则执行以下代码
        return []

#处理数据模块，传入数据data进行处理
def process_data(data):
    job_data = {}   #把提取到的数据保存到字典中
    job_data["城市"] = data["city"]
    job_data["公司名称"] = data["company"]
    job_data["学历要求"] = data["edu"]
    job_data["工作经验"] = data["exp"]
    job_data["招聘岗位"] = data["jobName"]
    job_data["薪资待遇"] = data["salary"]
    #获取招聘详情信息
    job_url = data["detailUrl"]
    job_res = responsibility(job_url)
    print(job_data)
    print(job_res)
    return job_data

#对详情页进行爬取
def responsibility(job_url):
    detail_res = requests.get(job_url,headers=headers)
    bs = BeautifulSoup(detail_res.text,"html.parser")
    #查找scripts标签，而不是section标签，因为使用了ajax进行反爬
    scripts = bs.find_all("script")#查找所有script标签
    text = ""
    #通过特殊值“window.pageData”找到我们需要的标签
    for script in scripts:
        if "window.pageData" in script.text:
            text = script.text
    
    start = text.find("window.pageData = ")+len("window.pageData = ")
    end = text.find(" || {}")
    job_des = text[start:end]#字符串的切片
    data = json.loads(job_des)  #使用json.loads方法转化字符串为python字典
    time.sleep(0.5)
    return data["desc"]

def while_data():
    #创建一个列表存放所有的职位信息
    all_data = []

    for i in range(1,30):
        data = send_get(i)
        if data:  #如果有信息，则返回True,没有返回False
            for item in data: #对职位列表进行遍历，遍历得到的是每一条职位信息
                try:
                    job = process_data(item)
                    all_data.append(job)
                except:
                    break
    return all_data

total_data = while_data()
df = pd.DataFrame(total_data)
df.to_excel("job.xlsx",index=False)
