# -*- coding: utf-8 -*-
"""
Created on Sun Oct  2 09:28:11 2022

@author: KateB
"""
# import pandas for parsing of model output
import pandas as pd
# import json to write json file
import json

# create_json accepts the path to the csv file --> this may be something we can
# change to be just a pd dataFrame in the future. Additionally, it needs the 
# image file name, height and width, and the output file name for the json file
def create_json(csv_path, input_file_path, img_height, img_width, file_name):
    # just add the file type
    json_path = filename + ".json"
    # import the data
    metadata = pd.read_csv(csv_path)
    # pull unique labels in case things are wonky
    features = metadata['label'].unique()
    # start the header of the file
    running_string = "{\"version\": \"5.0.1\", \"flags\": {}, \"shapes\": ["
    # iterate through each shape
    for feature in features:
        running_string += "{\"label\": \"" 
        # query just the single shape based on label name
        metadata_subset = metadata.query("label == {}".format(feature))
        # there should be only one value each -- we may need to go in and 
        # adjust how we approach this if things get weird.
        start_x = str(metadata_subset["start_x"])
        start_y = str(metadata_subset["start_y"])
        end_x = str(metadata_subset["end_x"])
        end_y = str(metadata_subset["end_y"])
        # add the shape name
        running_string += feature
        running_string += "\"", \"points\": [["
        # add the bounding boxes as in the legend
        running_string += start_x
        running_string += ", "
        running_string += start_y
        running_string += "],["
        running_string += end_x
        running_string += ", "
        running_string += end_y
        running_string += "]], \"group_id\": null, \"shape_type\": \"rectangle\", \"flags\": {}},"
    # the above loop adds an extra comma that we need to get rid of.
    running_string = running_string[:-1]
    # append the final data to the string
    running_string += "], \"imagePath\": \""
    running_string += input_file_path
    running_string += "\", \"imageData\": null, \"imageHeight\": "
    running_string += str(img_height)
    running_string += ", \"imageWidth\": "
    running_string += str(img_width)
    running_string += "}"
    # convert the string to a python-dict json-style
    running_json = json.loads(running_string)
    # convert the python-dict to json then write to the file    
    with open(json_path, "w") as running_json_dumped:
        json.dump(running_json, running_json_dumped)
        