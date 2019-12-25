# geology
Aims to predict areas with high likelihood of ore deposits based on multiple datasets.

### Datasets required:
- Major mineral deposits of the world - https://mrdata.usgs.gov/major-deposits/
- Current satellite data - Sentinel 2 / MODIS
- Digital elevation model - https://ecat.ga.gov.au/geonetwork/srv/eng/catalog.search#/metadata/66006
- Geological map - https://ccgm.org/en/home/168-lithological-map-of-the-world-9782917310250.html
- Soil map - https://nationalmap.gov/small_scale/atlasftp.html?openChapters=chpgeol%2Cchpbio%2Cchpwater#chpwater
- Previous locations of the current deposit point - https://www.earthbyte.org/paleomap-paleoatlas-for-gplates/
- Previous estimated climate - https://www.earthbyte.org/paleomap-paleoatlas-for-gplates/
- Volcanic activity - http://volcano.oregonstate.edu/volcano_table
- Hydrothermal activity - https://www.dmp.wa.gov.au/Petroleum/Geothermal-energy-2249.aspx?fbclid=IwAR2lsLKLYqA8tM25z5Tbm9iw2Q66JQqJym1M06-0gtGd2wZfbNfz8jq2Ohc
- Groundwater - http://www.bom.gov.au/water/groundwater/explorer/map.shtml
- Seismic activity - https://www.kaggle.com/usgs/earthquake-database/downloads/earthquake-database.zip/1
- Magnetic anomolies - https://www.dmp.wa.gov.au/Geological-Survey/Regional-geophysical-survey-data-1392.aspx
- Gravitational anomalies - https://www.dmp.wa.gov.au/Geological-Survey/Regional-geophysical-survey-data-1392.aspx
- Direction of current continental movement
- Vegetation indices (perhaps minerals in the soil affect this) - From Sentinel images / MODIS
- Geospatial indices (calculated from above data)

### Steps:
1. Gather data.
2. Preprocess data.
3. Feature engineer.
4. Build data pipeline.
5. Test different model types.
6. Apply best model to large area.
