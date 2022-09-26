import requests
from bs4 import BeautifulSoup

URL = "https://docs.bokeh.org/en/latest/index.html"
r = requests.get(URL)
print(r.content)  # print r.content to get the raw HTML content of the webpage. It is of ‘string’ type.

soup = BeautifulSoup(r.content,
                     'html5lib')  # If this line causes an error, run 'pip install html5lib' or install html5lib
print(soup.prettify())

# Python program to scrape website
# and save quotes from website
import csv

r = requests.get(URL)

soup = BeautifulSoup(r.content, 'html5lib')

quotes = []  # a list to store quotes

table = soup.find('div', attrs={'id': 'all_quotes'})

for row in table.findAll('div',
                         attrs={'class': 'col-6 col-lg-3 text-center margin-30px-bottom sm-margin-30px-top'}):
    quote = {'theme': row.h5.text, 'url': row.a['href'], 'img': row.img['src'], 'lines': row.img['alt'].split(" #")[0],
             'author': row.img['alt'].split(" #")[1]}
    quotes.append(quote)

filename = 'inspirational_quotes.csv'
with open(filename, 'w', newline='') as f:
    w = csv.DictWriter(f, ['theme', 'url', 'img', 'lines', 'author'])
    w.writeheader()
    for quote in quotes:
        w.writerow(quote)
