from django.db import models

# Create your models here.
from django.db import models
import os
from rest_framework.response import Response
import json


# Create your models here.

def Field_Creation_Model(Field_Creation):
    "Convert Json file received from Front End to Usable Json File to be Uploaded to the Interface"
    " Example of How the JSON file would look like "# Field_Creation = {"name": ['Corn_Field'], "coordinates": [['29.64836334', '49.59981966'],
    # ['29.64472203', '49.59762156'],
    # ['29.64900592', '49.59266969'],
    # ['29.65536334', '49.59985566']]}


    Field_Dict = {}
    Field_Coordinates = Field_Creation['coordinates']
    First_Coordinate = Field_Creation['coordinates'][0]
    Last_Coordinate_Index = int(len(Field_Coordinates)) - 1
    if Field_Coordinates[0] == Field_Coordinates[Last_Coordinate_Index]:
        pass
    else:
        Field_Coordinates.append(First_Coordinate)

    Field_Dict['coordinates'] = Field_Coordinates
    return Response(Field_Dict)
