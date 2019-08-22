# Import libraries.
import pandas as pd
import os
import matplotlib.pyplot as plt
from sentinelsat import SentinelAPI
os.getcwd()
# Read in geology csv.
df = pd.read_csv("data/geological/ofr20051294/deposit.csv")

plt.scatter(df["longitude"].values, df["latitude"].values)

tile_size = 0.02

# Create bounds 
if not os.path.exists("geology_footprints.csv"):
    df = df[["dep_name", "country", "latitude", "longitude", "commodity", "dep_type"]]
    df["upper left lat"] = df["latitude"] - tile_size
    df["upper left long"] = df["longitude"] + tile_size
    
    df["upper right lat"] = df["latitude"] + tile_size
    df["upper right long"] = df["longitude"] + tile_size
    
    df["lower right lat"] = df["latitude"] + tile_size
    df["lower right long"] = df["longitude"] - tile_size
    
    df["lower left lat"] = df["latitude"] - tile_size
    df["lower left long"] = df["longitude"] - tile_size
    df["wkt"] = 0
    for i in df.index:
        if i % 100 == 0:
            print(i)
        df["wkt"][i] = f'''Polygon(({df["lower left lat"][i]} {df["lower left long"][i]},{df["lower right lat"][i]} {df["lower right long"][i]},{df["upper right lat"][i]} {df["upper right long"][i]},{df["upper left lat"][i]} {df["upper left long"][i]}))'''

    df.to_csv("geology_footprints.csv")
    
df = pd.read_csv("geology_footprints.csv")
df.set_index("Unnamed: 0", inplace=True)
footprint = df["wkt"][0]

footprint = f"POINT ({df['longitude'][0]} {df['latitude'][0]})"
api = SentinelAPI(username, password, 'https://scihub.copernicus.eu/dhus')
# search by polygon, time, and SciHub query keywords
products = api.query(footprint,
                     platformname='Sentinel-2',
                     area_relation='Intersects',
                     cloudcoverpercentage=(0, 10))

products_df = api.to_dataframe(products)

# sort and limit to first 5 sorted products
products_df_sorted = products_df.sort_values(['cloudcoverpercentage', 'ingestiondate'], ascending=[True, True])
api.download(products_df_sorted.index[0])

