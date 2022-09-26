import requests
from bs4 import BeautifulSoup

URL = "https://docs.bokeh.org/en/latest/index.html"

# Making a GET request
r = requests.get(URL)

# Parsing the HTML
soup = BeautifulSoup(r.content, 'html.parser')

# find all the anchor tags with "href"
for link in soup.find_all('a'):
    print(link.get('href'))

# import requests
# from bs4 import BeautifulSoup
#
#
# # Making a GET request
# r = requests.get('https://www.geeksforgeeks.org/python-programming-language/')
#
# # Parsing the HTML
# soup = BeautifulSoup(r.content, 'html.parser')
#
# # find all the anchor tags with "href"
# for link in soup.find_all('a'):
# 	print(link.get('href'))
