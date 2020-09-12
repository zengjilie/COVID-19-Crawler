import requests
import json
import openpyxl
url_in = 'https://api.inews.qq.com/newsqa/v1/query/inner/publish/modules/list?modules=chinaDayList,chinaDayAddList,cityStatis,nowConfirmStatis,provinceCompare'
url_out = 'https://api.inews.qq.com/newsqa/v1/automation/modules/list?modules=FAutoGlobalStatis,FAutoContinentStatis,FAutoGlobalDailyList,FAutoCountryConfirmAdd'


response = requests.get(url_in)
response = response.text
response = json.loads(response)
print(type(response))

data = response['data']
chinaDayAddList = data['chinaDayAddList']
# print(chinaDayAddList)

wb = openpyxl.Workbook()
ws = wb.active
ws.title = '国内疫情趋势数据'
ws.append(['date','confirmed','imported','heal'])

dateList = []
confirmedList = []
importedList = []
healList = []
for each in chinaDayAddList[150:]:
    date = each['date']
    date = date
    dateList.append(date)

    confirmed = each['confirm']
    confirmedList.append(confirmed)  
    
    imported = each['importedCase']
    importedList.append(imported) 
      
    heal = each['heal']
    healList.append(heal) 

print(len(importedList))

dateList = str(dateList)
confirmedList = str(confirmedList)
importedList = str(importedList)
healList = str(healList)
ws.append([dateList,confirmedList,importedList,healList]) 

#全球数据            
response_out = requests.get(url_out)
response_out = response_out.text
response_out = json.loads(response_out)


data_out = response_out['data']
globalList= data_out['FAutoGlobalDailyList']
print(globalList)

#新增工作表
ws_out = wb.create_sheet('国外疫情趋势')

ws_out.append(['date','confirmed','newAddConfirm','heal'])

dateList_out = []
confirmedList_out = []
newConfimList_out = []
healList_out = []
for each in globalList[150:]:
    date = each['date']
    dateList_out.append(date)

    confirmed = each['all']['confirm']
    confirmedList_out.append(confirmed)  
    
    newConfirm = each['all']['newAddConfirm']
    newConfimList_out.append(newConfirm) 
      
    heal = each['all']['heal']
    healList_out.append(heal) 

dateList_out = str(dateList_out)
confirmedList_out = str(confirmedList_out)
newConfimList_out = str(newConfimList_out)
healList_out = str(healList_out)

ws_out.append([dateList_out,confirmedList_out,newConfimList_out,healList_out])

wb.save('./addData.xlsx')
    

