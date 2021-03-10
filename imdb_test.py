from bs4 import BeautifulSoup
import requests
import csv
import re

source = requests.get('https://www.imdb.com/search/name/?birth_monthday=03-07&ref_=nv_cel_brn').text
soup = BeautifulSoup(source, 'lxml')
# print(soup.prettify())

# csv_file = open('imdb_list', 'w')

# csv_writer = csv.writer('csv_file')
# csv_writer.writerow('name', 'summary,'link')

article = soup.find('div', class_='article')
headline = article.h1.text

list = article.find('div', class_='lister-item-content')
a_name = list.h3.a.text


list_sum = list.find_all('p')[1]

print(list_sum)
