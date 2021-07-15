import requests #라이브러리 가져오기
from bs4 import BeautifulSoup #라이브러리 가져오기

name = 'hyojun'
url = f'https://api.nationalize.io/?name={name}'

response = requests.get(url).json()
a = response['country']
b = a[0]

print(b['country_id'])