# Import libraries.
import pandas as pd
import os
import matplotlib.pyplot as plt
from sentinelsat import SentinelAPI
import rasterio
from rasterio.plot import show
import shapely
from shapely.geometry import box
from rasterio.enums import Resampling

df = pd.read_csv("USGS_REE_US_CSV/Loc_Pt.csv")

df["Commodity"].value_counts()