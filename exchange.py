import requests #라이브러리 가져오기
from bs4 import BeautifulSoup #라이브러리 가져오기

url = 'https://finance.naver.com/marketindex/'
response = requests.get(url).text # 요청 보내고 받은 응답 text 변환
data = BeautifulSoup(response, 'html.parser') # 응답으로 받은 걸 처리하기 쉽게 가공(parsing)
exchange = data.select_one('#exchangeList > li.on > a.head.usd > div > span.value') 
result = exchange.text

print(f'현재 원/달러 환율은 {result} 입니다.')