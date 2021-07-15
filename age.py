import requests #라이브러리 가져오기
from bs4 import BeautifulSoup #라이브러리 가져오기

name = 'allen'
url = f'https://api.agify.io/?name={name}'

response = requests.get(url).json()

print(response)
print(response['age'])