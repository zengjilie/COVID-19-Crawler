import requests
import openpyxl
import json
from lxml import etree
import re

wb = openpyxl.Workbook()
ws = wb.active
ws.title = '问答'
ws.append(['question'])

url="https://dxy.com/disease/24677/detail/0/1-1"
response = requests.get(url)
response = response.text

#形成xml树
html = etree.HTML(response)


q = html.xpath('//div[@class="html-parse tag-html"]/h2/text()')
a = html.xpath('//div[@class="html-parse tag-html"]//p/text()')



#print(a)
q_re = []
for each in q:  
    qq = re.sub("([0-9]+\.|R)","",each,re.S) 
    q_re.append(qq)

    ws.append([qq])
print(q_re)

ws_a = wb.create_sheet("回答")
ws_a.append(['answer'])
for each in a:
    ws_a.append([each])

wb.save('./q-a.xlsx')