#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import csv
import pandas as pd
import plotly_express as px
import plotly.graph_objects as go

 # Assuming you have a file "washington_cities.py" with city coordinates
from washington_cities import locations 


FILENAME = "Electric_Vehicle_Data.csv"

def city_counts(FILENAME):
    
    """
    Parameters:
    FILENAME: csv file being imported
    
    Count the number of electric vehicles in each city
    
    Returns: Dictionary with cities as keys and their electric vehicle counts as values
    """
    
    fin_list = []
    
    # Opening file
    with open(FILENAME, 'r') as f:
        reader = csv.reader(f)
        
        # Skip header
        next(reader)  

        # Going through every line and counting electric vehicles in each city
        for line in reader:
            
            fin_list.append(line)
    
    dct = {}
    
    for data in fin_list:
        
        city_name = data[2]
        
        # Skip entries with empty city names
        if city_name == '':
            
            continue
        
        elif city_name in dct:
            
            dct[city_name] += 1
            
        else:
            
            dct[city_name] = 1
        
    return dct

def heatmap(dct):
    
    """
    Parameters:
    dct: Dictionary with cities as keys and their electric vehicle counts as values
    
    Create a heatmap using Plotly Express with city coordinates and electric vehicle counts
    
    """
    
    cities = []
    ev_pop = []
    lat = []
    long = []
    
    for city in dct:
        
        for city_lat_long in locations:
            
            # Assuming that the city coordinates are stored in the 'locations' dictionary
            if city_lat_long.startswith(city):
                
                lat.append(locations[city_lat_long][0])
                long.append(locations[city_lat_long][1])
                cities.append(city)
                ev_pop.append(dct[city])
    
    # Creating a DataFrame for Plotly Express
    data = {
        'City': cities,
        'EV_Population': ev_pop,
        'Latitude': lat,
        'Longitude': long
    }
    
    df = pd.DataFrame(data)
    
    # Creating a density map using Plotly Express
    fig = px.density_mapbox(df, lat='Latitude', lon='Longitude', z='EV_Population', radius=10,
                            center=dict(lat=df.Latitude.mean(), lon=df.Longitude.mean()),
                            zoom=2, mapbox_style='open-street-map', height=900)
    
    # Add a scatter plot on top of the density map to represent each city's EV population with markers
    # Added to visually represent cities with smaller EV populations
    fig.add_trace(
    go.Scattermapbox(
        lat=df["Latitude"],
        lon=df["Longitude"],
        mode="markers",
        showlegend=False,
        hoverinfo="skip",
        marker={
            "color": df["EV_Population"],
            "size": df["EV_Population"].fillna(0),
            "coloraxis": "coloraxis",
            "sizeref": (df["EV_Population"].max()) / 15 ** 2,
            "sizemode": "area",
        },
    )
    )
    
    # Displaying the heatmap
    fig.show()
    
    
if __name__ == "__main__":
    
    # Counting electric vehicles in each city and creating a heatmap
    dct = city_counts(FILENAME)
    heatmap(dct)