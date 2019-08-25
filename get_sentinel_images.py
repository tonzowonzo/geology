# Import libraries.
import pandas as pd
import os
import matplotlib.pyplot as plt
from sentinelsat import SentinelAPI
import rasterio
from rasterio.plot import show
import shapely
from shapely.geometry import box

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

api = SentinelAPI(username, password, 'https://scihub.copernicus.eu/dhus')

for i in df.index:
    footprint = f"POINT ({df['longitude'][i]} {df['latitude'][i]})"
    
    # search by polygon, time, and SciHub query keywords
    products = api.query(footprint,
                         platformname='Sentinel-2',
                         area_relation='Intersects',
                         cloudcoverpercentage=(0, 5))
    
    products_df = api.to_dataframe(products)
    
    # sort and limit to first 5 sorted products
    products_df_sorted = products_df.sort_values(['cloudcoverpercentage', 'ingestiondate'], ascending=[True, True])
    api.download(products_df_sorted.index[0])

    # Clip the images
    img_name = products_df_sorted.title[0].split(".")[0] 
    for img_loc in os.listdir(f"data/satellite/" + img_name + ".SAFE" + "/GRANULE/"):
        for img in os.listdir(f"data/satellite/" + img_name + ".SAFE" + "/GRANULE/" +
                              img_loc + "/IMG_DATA/"):
            output_location = f"data/satellite/clipped_{df["]}"
            # Load in image to be clipped.
            data = rasterio.open(f"data/satellite/" + img_name + ".SAFE" + "/GRANULE/" +
                              img_loc + "/IMG_DATA/" + img)
            show((data, 1), cmap='terrain')
            # Create bounding box for clipping image.
            minx, miny = df["lower left lat"][i], df["lower left long"][i]
            maxx, maxy = df["upper right lat"][i], df["upper right long"][i]
            bbox = box(minx, miny, maxx, maxy)
            
            