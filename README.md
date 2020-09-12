
# COVID-19 Data Crawler for personal project 'COVID Kit'

This project is the data prepared for the development of my personal WeChat mini-program COVID Kit, which includes domestic and international epidemic data, CCTV videos with the keyword "COVID-19", popular scientific knowledge and common questions about COVID-19.

* Epidemic data comes from [Baidu](https://voice.baidu.com/act/newpneumonia/newpneumonia), [Tencent](https://news.qq.com/zt2020/page/feiyan.htm#/? nojump=1)

* Videos comes from [CCTV Video](https://v.cctv.com/sousuo/index.shtml?title=%E6%96%B0%E5%86%A0)

* Popular science knowledge comes from [Baidu Health](https://www.baidu.com/bh/dict/ydxx_8829639274010099959?tab=%E6%97%A5%E5%B8%B8&title=%E6%96%B0%E5% 9E%8B%E5%86%A0%E7%8A%B6%E7%97%85%E6%AF%92%E8%82%BA%E7%82%8E&contentid=ydxx_8829639274010099959&sf_ref=dict_home&from=dicta) and [(new coronavirus Viral pneumonia diagnosis and treatment plan (trial eighth edition)](http://www.gov.cn/zhengce/zhengceku/2020-08/19/5535757/files/da89edf7cc9244fbb34ecf6c61df40bf.pdf)

* FQAs come from [Doctor Dingxiang](https://m.dxy.com/disease/24677/detail/0/1-1)

```python
mainData.py
```

Daily epidemic data (non-dynamic)

```python
trendData.py
```

Data from January to the current day (in this project I start recording from June)

```python
QA.py
```

Data of FQAs from Doctor Dingxiang

```python
video.py
downloadVideo.py
```

Data of CCTV video link
