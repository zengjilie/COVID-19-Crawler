import os, sys
from moviepy.editor import *
import numpy as np
import openpyxl
import requests
import re
import json
import time
f = open(r'C:/Users/USER/Desktop/爬取疫情数据/数据json/video/data.json','r')#下载下来的json数据
f = f.read()
f = re.sub(r"\[|\]","",f)#去掉多余的方括号
f = f.split(',')#转成数组
head = {
    "Accept":" */*",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "zh,en;q=0.9,en-US;q=0.8,zh-CN;q=0.7,zh-TW;q=0.6",
    "Cache-Control": "no-cache",
    "Connection": "keep-alive",
    "Cookie": "cna=7pbJFlfXUVUCAd9oFJDU6bBO; cn_1259451800_dplus=%7B%22distinct_id%22%3A%20%22174339cb14b2b6-05d964c75d5216-3323766-1fa400-174339cb14c4d7%22%7D; UM_distinctid=174339cb14b2b6-05d964c75d5216-3323766-1fa400-174339cb14c4d7; sca=c0367a46",
    "Host": "media.app.cctv.com",
    "Pragma": "no-cache",
    "Referer": "https://v.cctv.com/sousuo/index.shtml?title=%E6%96%B0%E5%86%A0",
    "Sec-Fetch-Dest": "script",
    "Sec-Fetch-Mode": "no-cors",
    "Sec-Fetch-Site": "same-site",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36"
}
wb = openpyxl.Workbook()
ws = wb.active
ws.title = '视屏链接'
ws.append(['URL','image1','mediaImg','mediaName','pubTime','title','vduration'])
for each in f:
    each = json.loads(each)#转成字典
    url = each['URL']
    response = requests.get(url,head,verify = False)#不验证ssl证书
    response = response.text
    m = re.sub("main\.m3u8\?maxbr=2048","2000.m3u8",url)#改成需要的文件
    m = re.sub("main","2000",m)
    print(m)
    ws.append([m])

#在文件夹中复制地址时，文件夹中的地址是用 \ 来分隔不同文件夹的，而Python识别地址时只能识别用 / 分隔的地址


#打开videoinfo文件
vf = open(r'C:/Users/USER/Desktop/爬取疫情数据/数据json/video/videoinfo.json','r')
ws_vf = wb.create_sheet('视屏资料')
ws_vf.append()

#处理请求
vf = vf.read()
vf = re.sub(r"\[|\]","",vf)
vf = vf.split(',')

#发送请求
for each in vf:
    each = json.loads(each)
    url = each["URL"]
    #请求
    response = requests.get(url,head,verify=False)
    response.close()
    #处理数据
    response = response.text
    response = re.sub('(t\d*\()|\)','',response)
    response = json.loads(response)
    data = response['data']
    
    for each in data:
    #图片 image1
    #媒体logo mediaImg
    #媒体名称 mediaName
    #日期 pubTime
    #标题 title
    #视屏长度 vduration
        image = each['image1']
        mediaImg = each['mediaImg']
        mediaName = each['mediaName']
        pubTime = each['pubTime']
        title = each['title']
        vduration = each['vduration']
        ws_vf.append([image,mediaImg,mediaName,pubTime,title,vduration])
        print("wancheng")
        
    time.sleep(2)
    


wb.save('./videoData.xlsx')
# print(sys.path[0])
#不加r的话会转译生效
# os.mkdir(r"C:\Users\USER\Desktop\爬取疫情数据\video") 
# url = 'https://hls.cntv.lxdns.com/asp/hls/2000/0303000a/3/default/90b9b0a51ed6428986603865a7566777/2000.m3u8'
# response = requests.get(url)
# response = response.text
# print(response)
# ts = re.findall('(\d).ts',response)


# for i in ts:
#     url_ts = re.sub('2000.m3u8','%s.ts'%(i),url)
#     print(url_ts)
#     response_ts = requests.get(url_ts,stream=True)
#     with open('./video','w') as f:
#         f.wirte(url_ts)
