# geology
Aims to predict areas with high likelihood of ore deposits based on multiple datasets.

### Datasets required:
- Major mineral deposits of the world - https://mrdata.usgs.gov/major-deposits/
- Current satellite data - Sentinel 2
- Digital elevation model - https://www.eorc.jaxa.jp/ALOS/en/aw3d30/data/index.htm
- Previous locations of the current deposit point - https://www.earthbyte.org/paleomap-paleoatlas-for-gplates/
- Previous estimated climate - https://www.earthbyte.org/paleomap-paleoatlas-for-gplates/
- Volcanic activity
- Seismic activity
- Magnetic anomolies - https://www.ngdc.noaa.gov/geomag/emag2.html?fbclid=IwAR1gseHiQ9vb0mCY0-ZrM9j7kjxhS3Gyry1bWKhYeFeH_QY6gALwT7rwwLk
- Direction of current continental movement
- Vegetation indices (perhaps minerals in the soil affect this)
- Geospatial indices (calculated from above data)

### Steps:
1. Gather data.
2. Preprocess data.
3. Feature engineer.
4. Build data pipeline.
5. Test different model types.
6. Apply best model to large area.
