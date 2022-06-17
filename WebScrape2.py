import requests
from bs4 import BeautifulSoup
import texttable as tt

# Code to access HTML content of a webpage
URL = "https://www.worldometers.info/coronavirus/countries-where-coronavirus-has-spread/"
r = requests.get(URL)
# print(r.content)

soup = BeautifulSoup(r.content, 'html5lib')
# print(soup.prettify())

data = []
data_iterator = iter(soup.find_all('td'))
while True:
    try:
        country = next(data_iterator).text
        confirmed = next(data_iterator).text
        deaths = next(data_iterator).next
        continent = next(data_iterator).next

        data.append((country,
                     int(confirmed.replace(',', '')),
                     int(deaths.replace(',', '')),
                     continent))
    except StopIteration:
        break

data.sort(key= lambda row: row[1], reverse= True)

table = tt.Texttable()

# Add an empty row at the beginning for the headers
table.add_rows([(None, None, None, None)] + data)

# 'l' denotes left, 'c' denotes center,
# and 'r' denotes right
table.set_cols_align(('c', 'c', 'c', 'c'))
table.header((' Country ', ' Number of cases ', ' Deaths ', ' Continent '))

print(table.draw())
