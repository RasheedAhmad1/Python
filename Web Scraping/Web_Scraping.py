# Scrap or Extract data from a website

# Import some useful libraries
from bs4 import BeautifulSoup as bs4
import requests
import pandas as pd

pages = []

pages_to_scrap = 5

for i in range(1, pages_to_scrap+1):
    url = ('http://books.toscrape.com/catalogue/page-{}.html').format(i)
    pages.append(url)
    print(pages)
