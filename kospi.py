import requests #라이브러리 가져오기
from bs4 import BeautifulSoup #라이브러리 가져오기

url = 'https://finance.naver.com/sise/'
response = requests.get(url).text # 요청 보내고 받은 응답 text 변환
data = BeautifulSoup(response, 'html.parser') # 응답으로 받은 걸 처리하기 쉽게 가공(parsing)
kospi = data.select_one('#KOSPI_now')
kosdaq = data.select_one('#KOSDAQ_now')
# popitem = data.select_one('#popularItemList > li:nth-child(1) > a')

print(f'현재 코스피 지수는 {kospi.text}이고 코스닥 지수는 {kosdaq.text} 입니다.\n')
print("인기종목은: ")

for i in range(1, 11):
    popitem = data.select_one(f'#popularItemList > li:nth-child({i}) > a')
    print(popitem.text)