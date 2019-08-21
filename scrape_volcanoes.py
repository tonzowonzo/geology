# Import libraries.
import requests
import bs4
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
import pandas as pd
html = requests.get("http://volcano.oregonstate.edu/volcano_table").content
soup = BeautifulSoup(html, "lxml")
df = []

# Find columns.
for i, table in enumerate(soup.find_all("tr")):
    lst  = []
    # Find rows.
    for j, row in enumerate(table.children):
        # If it has no tag, ignore it.
        if isinstance(row, bs4.NavigableString):
            continue
        # If it's in one of these columns.
        elif j in [3, 5, 7, 9, 11]:
            print(j, row.contents)
            row = row.string
            if not row:
                pass
            else:
                row = row[5:].strip()
            lst.append(row)
    df.append(lst)
    
df = pd.DataFrame(df)
df.columns = df.iloc[0]
df.drop(df.index[0], inplace=True)
df = df[df["Latitude (dd)"] != ""]
df["Longitude (dd)"] = df["Longitude (dd)"].astype(float)
df["Latitude (dd)"] = df["Latitude (dd)"].astype(float)
df["Elevation (m)"] = df["Elevation (m)"].astype(float)

df.to_csv("volcanoes.csv")
#df = df[[1, 3, 5, 7, 9, 11]]

plt.scatter(df["Longitude (dd)"].values, df["Latitude (dd)"].values)
