import streamlit as st
from PIL import Image
import requests

import pathlib
    
import geemap.foliumap as geemap
import ee

st.title('Global Normalised Difference Vegetation Index')
m = geemap.Map(height=800)

year = st.slider("Select the year", 1985, 2013, 2000)
st.text(f"Normalised difference vegetation index (NDVI) is a widely-used indicator to look at the health and density of vegetation. The map shows global NDVI for the year {year}, from the AVHRR satellite.")
        
dataset = ee.ImageCollection('NASA/GIMMS/3GV0').filter(ee.Filter.date(f'{year}-06-01', f'{year}-12-31'))
ndvi = dataset.select('ndvi')
ndviVis = {
  'min': -1.0,
  'max': 1.0,
  'palette': ['000000', 'f5f5f5', '119701'],
}
m.setCenter(-88.6, 26.4, 1)
m.addLayer(ndvi, ndviVis, 'NDVI')

m.to_streamlit()
