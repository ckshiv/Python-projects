import requests
from bs4 import BeautifulSoup
import csv

# Code to access HTML content of a webpage
URL = "http://www.values.com/inspirational-quotes"
r = requests.get(URL)
# print(r.content)

# Parsing HTML content
soup = BeautifulSoup(r.content, 'html5lib')
# print(soup.prettify())

# Code to get list of quotes from the result
quotes = []  # to store the quotes
table = soup.find('div', attrs={'id': 'all_quotes'})
# print(table.prettify())
for row in table.findAll('div', attrs={'class': 'col-6 col-lg-3 text-center margin-30px-bottom sm-margin-30px-top'}):
    quote = {}
    quote['theme'] = row.h5.text
    quote['url'] = row.a['href']
    quote['img'] = row.img['src']
    quote['line'] = row.img['alt'].split(" #")[0]
    quote['author'] = row.img['alt'].split(" #")[1]
    quotes.append(quote)

filename = 'inspirational_quotes.csv'
with open(filename, 'w', newline= '') as f:
    w = csv.DictWriter(f, ['theme', 'url', 'img', 'lines', 'author'])
    w.writeheader()
    for quote in quotes:
        w.writerow(quote)
