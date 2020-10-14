import requests
from bs4 import BeautifulSoup

# 타겟 URL을 읽어서 HTML를 받아오고,
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://movie.naver.com/movie/sdb/rank/rmovie.nhn?sel=pnt&date=20200716',headers=headers)

# HTML을 BeautifulSoup이라는 라이브러리를 활용해 검색하기 용이한 상태로 만듦
# soup이라는 변수에 "파싱 용이해진 html"이 담긴 상태가 됨
# 이제 코딩을 통해 필요한 부분을 추출하면 된다.
soup = BeautifulSoup(data.text, 'html.parser') #xml도 된다.

tr = soup.select_one('#old_content > table > tbody > tr:nth-child(2) > td.title > div > a')
movies = soup.select('#old_content > table > tbody > tr')
#print(movies)
#old_content > table > tbody > tr:nth-child(2) > td.title > div > a
#old_content > table > tbody > tr:nth-child(2)
#old_content > table > tbody > tr:nth-child(2) > td:nth-child(1) > img

#body-content > div.newest-list > div > table > tbody > tr:nth-child(1) > td.number

for movie in movies:
    movie_name = movie.select_one('td.title > div > a')

    #movie_rank = movie.select_one('td:nth-child(1) > img')['alt']
    # old_content > table > tbody > tr:nth-child(2) > td.point
    if movie_name is None #and movie_rank is None:
        continue
    else:
        movie_rank = movie.select_one('td.ac > img')['alt']
        score = movie.select_one('td.point')
        print(score)
        print(movie_rank)
        print(movie_name.text)

#print(tb)
#print(tr.text)
#############################
# (입맛에 맞게 코딩)
#############################