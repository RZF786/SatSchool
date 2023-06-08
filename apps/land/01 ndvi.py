import streamlit as st
from PIL import Image
import requests

import pathlib
    
import geemap.foliumap as geemap
import ee

st.title('Global Normalised Difference Vegetation Index for 2013')
m = geemap.Map(height=800)

dataset = ee.ImageCollection('NASA/GIMMS/3GV0').filter(ee.Filter.date('2013-06-01', '2013-12-31'))
dataset_ndvi = dataset2019.select('ndvi')

ndvi = dataset.select('ndvi');
ndviVis = {
  'min': -1.0,
  'max': 1.0,
  'palette': ['000000', 'f5f5f5', '119701'],
}
m.setCenter(-88.6, 26.4, 1);
m.addLayer(ndvi, ndviVis, 'NDVI');

m.to_streamlit()
