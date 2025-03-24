import requests
from bs4 import BeautifulSoup
import csv 

url = "https://www.grobmart.com/Buku"
response = requests.get(url)
soup = BeautifulSoup(response.content , "html.parser")

buku_cointainer = soup.find_all("div",class_="product-thumb")

with open('buku.csv','w',newline='',encoding='utf-8') as csv_file:
    writer = csv.writer(csv_file)
    
    for container in buku_cointainer :
        title = container.find('div','name').text
        print(title)

