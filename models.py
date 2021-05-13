from django.db import models

# Create your models here.
from django.db import models
import os
from rest_framework.response import Response
import json
from shapely.geometry import Polygon
import numpy as np
from pyproj import Proj
from shapely.geometry import shape


# Create your models here.



def Field_Creation_Model(Field_Creation):
    "Convert Json file received from Front End to verifiable coordinates embed into a Json File to be Uploaded to the Interface"
    " Example of How the JSON file would look like "
    # Field_Creation = {"name": ['Corn_Field'], "coordinates": [['29.64836334', '49.59981966'],
    # ['29.64472203', '49.59762156'],
    # ['29.64900592', '49.59266969'],
    # ['29.65536334', '49.59985566']]}


    Field_Dict = {}
    # Validate that the coordinates is enclosed
    Field_Coordinates = Field_Creation['coordinates']
    First_Coordinate = Field_Creation['coordinates'][0]
    Last_Coordinate_Index = int(len(Field_Coordinates)) - 1
    if Field_Coordinates[0] == Field_Coordinates[Last_Coordinate_Index]:
        pass
    else:
        Field_Coordinates.append(First_Coordinate)

    Field_Dict['coordinates'] = Field_Coordinates
    return Response(Field_Dict)



def Calculate_Area_of_Coordinates(Field_Dict):
    "Receives json file from the Field_Creation_Model to calculate Area from the coordinates" 
    # Field_Creation = {"name": ['Corn_Field'], "coordinates": [['29.64836334', '49.59981966'],
    # ['29.64472203', '49.59762156'],
    # ['29.64900592', '49.59266969'],
    # ['29.65536334', '49.59985566']]}
    coord_str = []
    for i in range(len(Field_Dict['coordinates'])):
        x = Field_Dict['coordinates'][i][0]
        x  = float(x)
        y = Field_Dict['coordinates'][i][1]
        y = float(y)
        coordinate = (x,y)
        coord_str.append(coordinate)
    tuple(coord_str)
    
    def calc_area(coord_str):
        lons, lats = zip(*coord_str)
        ll = list(set(lats))[::-1]
        var = []
        for i in range(len(ll)):
            var.append('lat_' + str(i+1))
        st = ""
        for v, l in zip(var,ll):
            st = st + str(v) + "=" + str(l) +" "+ "+"
        st = st +"lat_0="+ str(np.mean(ll)) + " "+ "+" + "lon_0" +"=" + str(np.mean(lons))
        tx = "+proj=aea +" + st
        pa = Proj(tx)

        x, y = pa(lons, lats)
        cop = {"type": "Polygon", "coordinates": [zip(x, y)]}
        value = shape(cop).area 
        area_value = value/10000
        return(area_value)
    return Response(calc_area(coord_str))
