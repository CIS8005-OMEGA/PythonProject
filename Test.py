import requests
import numpy as np
import pandas as pd
try:
    from bs4 import BeautifulSoup
except ImportError:
    from BeautifulSoup import BeautifulSoup

page = requests.get("https://mcclintock.house.gov/newsroom/speeches")
soup = BeautifulSoup(page.content, 'html.parser')
print(soup)
