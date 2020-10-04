import requests
from bs4 import BeautifulSoup

url = 'https://search.daum.net/search?w=news&nil_search=btn&DA=NTB&enc=utf8&cluster=y&cluster_page=1&q=%EC%B6%94%EC%84%9D'
resp = requests.get(url)
news_bs = BeautifulSoup(resp.text, "html.parser")
title_list = news_bs.find_all('a', class_='f_link_b')  # 데이터가 리스트 형태로 온다
#print(title_list)
#print(1)
for i in title_list:
    #print(1)
    print(i.text)  # 리스트 형태기 때문에 for문을 통해 .text의 제목을 다 가져온다
