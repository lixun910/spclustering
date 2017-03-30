import json

"""
with open('columbus.geojson') as f:
    data = json.load(f)
    
for i in data["features"]:
    x = i["geometry"]["coordinates"]
    print '{"x": ', x[1], ', "y": ', x[0], '},'
""" 

import pysal
w = pysal.weights.Queen.from_shapefile("/Users/xunli/Downloads/columbus/columbus.shp")
for k in w.neighbors:
    for nn in w.neighbors[k]:
        print '{"source": ', k, ', "target": ', nn, '},'
        
dbf = pysal.open("/Users/xunli/Downloads/columbus/columbus.dbf", 'r')
data = dbf.by_col_array('HOVAL', 'INC', 'CRIME')

import sklearn
from sklearn.metrics.pairwise import cosine_similarity

dist = cosine_similarity(data)

print dist

for k in w.neighbors:
    for nn in w.neighbors[k]:
        print '{"source": ', k, ', "target": ', nn, ', "sim": ', dist[k][nn], '},'
        
