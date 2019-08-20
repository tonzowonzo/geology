# Import libraries.
import requests
from bs4 import BeautifulSoup
import pandas as pd
html = requests.get("http://volcano.oregonstate.edu/volcano_table").content
soup = BeautifulSoup(html, "lxml")
df = []

for i, table in enumerate(soup.find_all("tr")):
    lst  = []
    for row in table.children:
        print(row, i)
        lst.append(row)
    df.append(lst)
    
df = pd.DataFrame(df)
        
