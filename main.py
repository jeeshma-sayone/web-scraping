import requests
from bs4 import BeautifulSoup

URL = "https://docs.bokeh.org/en/latest/index.html"
r = requests.get(URL)
print(r.content)  # print r.content to get the raw HTML content of the webpage. It is of ‘string’ type.

soup = BeautifulSoup(r.content, 'html5lib') # If this line causes an error, run 'pip install html5lib' or install html5lib
print(soup.prettify())
