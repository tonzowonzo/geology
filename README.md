# geology
Aims to predict areas with high likelihood of ore deposits based on multiple datasets.

### Datasets required:
- Major mineral deposits of the world - https://mrdata.usgs.gov/major-deposits/
- Current satellite data - Sentinel 2
- Digital elevation model
- Previous locations of the current deposit point - Continental movement modelling
- Previous estimated climate
- Volcanic activity
- Seismic activity
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
