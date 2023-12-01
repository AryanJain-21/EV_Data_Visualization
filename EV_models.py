#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import csv
import matplotlib.pyplot as plt

FILENAME = "Electric_Vehicle_Data.csv"

def read_csv(FILENAME):
    """
    Parameters:
    FILENAME: csv file being imported
    
    Read in a csv file into dictionaries for electric vehicles and hybrid vehicles
    
    Returns: Two dictionaries, one for electric vehicles and one for hybrid vehicles
    """
    # Initializing variables
    ev_dct = {}
    hybrid_dct = {}
    
    # Opening file
    
    with open(FILENAME, 'r') as f:
        reader = csv.reader(f)
        
        # Skip header
        next(reader)  

        # Going through every line and categorizing data into dictionaries
        
        for line in reader:
            
            if 'PHEV' in line[8]:
                
                # Categorize hybrid vehicles, key = brand and values = models
                
                if line[6] in hybrid_dct:
                    
                    hybrid_dct[line[6]].append(line[7])
                    
                else:
                    
                    hybrid_dct[line[6]] = [line[7]]
                    
            else:
                
                # Categorize electric vehicles, key = brand and values = models
                
                if line[6] in ev_dct:
                    
                    ev_dct[line[6]].append(line[7])
                    
                else:
                    
                    ev_dct[line[6]] = [line[7]]
                
    return ev_dct, hybrid_dct

def type_of_car(FILENAME):
    
    """
    Parameters:
    FILENAME: csv file being imported
    
    Count and categorize the types of electric and hybrid vehicles
    
    Returns: Lists of types and their corresponding counts
    """
    
    fin_list = []
    
    # Opening file
    with open(FILENAME, 'r') as f:
        reader = csv.reader(f)
        
        # Skip header
        next(reader)  

        # Going through every line and adding to list to return
        for line in reader:
            fin_list.append(line)
    
    # Counting and categorizing types
    
    dct = {}
    
    for data in fin_list:
        
        car_type = data[8]
        
        if car_type in dct:
            
            dct[car_type] += 1
            
        else:
            
            dct[car_type] = 1
       
    types = []
    counts = []
    
    for data in dct:
        
        types.append(data)
        counts.append(dct[data])
        
    return types, counts

def model_amount(car_dct):
    
    """
    Parameters:
    car_dct: Dictionary of electric or hybrid vehicles
    
    Count the number of each model for electric or hybrid vehicles
    
    Returns: Dictionary with models as keys and their counts as values
    """
    
    car_model_dct = {}
    
    for brand in car_dct:
        
        for model in car_dct[brand]:
            
            if model in car_model_dct:
                
                car_model_dct[model] += 1
                
            else:
                
                car_model_dct[model] = 1
    
    return car_model_dct

def brand_amount(car_dct):
    
    """
    Parameters:
    car_dct: Dictionary of electric or hybrid vehicles
    
    Count the number of vehicles for each brand for electric or hybrid vehicles
    
    Returns: Dictionary with brands as keys and their counts as values
    """
    
    car_brand_dct = {}
    
    for brand in car_dct:
        car_brand_dct[brand] = len(car_dct[brand])
        
    return car_brand_dct

def most_sold_models(car_model_dct):
    
    """
    Parameters:
    car_model_dct: Dictionary with models as keys and their counts as values
    
    Find the top 3 most sold models
    
    Returns: Two lists, one of the most sold models, and the other of their counts
    """
    
    # Initializing variables
    var_max = 0
    var_max_model = ''
    var_models = []
    var_maxes = []
    
    # Finding the top 3 most sold models
    for x in range(3):
        
        # To track the maximum
        var_max = 0
        
        # Going through all the models
        for model in car_model_dct:
            
            # Making sure the model hasn't already been recorded
            if model in var_models:
                
                continue
            
            # The model is new and has a count greater than the recorded max so far
            elif var_max < car_model_dct[model]:
                
                # Assigning the maximum count and model for now
                var_max = car_model_dct[model]
                var_max_model = model
        
        # After running through the entire list of models, the highest sold model
        # is appended to the list along with its count
        
        var_models.append(var_max_model)
        var_maxes.append(var_max)
    
    # The list of models and their counts are returned
    
    return var_maxes, var_models
    
if __name__ == "__main__": 
    
    # Plotting bar chart for types of electric and hybrid vehicles
    counts, types = type_of_car(FILENAME)
    plt.bar(counts, types)
    plt.xticks(fontsize=8)
    plt.title("EV and Hybrid Vehicle Counts in Washington")
    plt.xlabel("Types")
    plt.ylabel("Counts")
    plt.show()

    # Analyzing and plotting most sold models for electric and hybrid vehicles
    ev_dct, hybrid_dct = read_csv(FILENAME)
    
    ev_model_dct = model_amount(ev_dct)
    hybrid_model_dct = model_amount(hybrid_dct)
    
    ev_models, ev_sold = most_sold_models(ev_model_dct)
    hy_models, hy_sold = most_sold_models(hybrid_model_dct)
    
    plt.bar(ev_sold, ev_models, color='blue', label='Electric Vehicles')
    plt.bar(hy_sold, hy_models, color='red', label='Hybrid Cars')
    plt.xticks(fontsize=8)
    plt.title("Top 3 EV Car Models and Top 3 Hybrid Car Models in Washington")
    plt.xlabel("Models")
    plt.ylabel("Amount Sold")
    plt.legend()
    plt.show()
    
    # Analyzing and plotting most sold brands for electric and hybrid vehicles
    ev_brand_dct = brand_amount(ev_dct)
    ev_brands, ev_sold2 = most_sold_models(ev_brand_dct)
    
    hy_brand_dct = brand_amount(hybrid_dct)
    hy_brands, hy_sold2 = most_sold_models(hy_brand_dct)
    
    plt.bar(ev_sold2, ev_brands, color='blue', label='EV Brands')
    plt.bar(hy_sold2, hy_brands, color='red', label='Hybrid Brands')
    plt.xticks(fontsize=8)
    plt.title("Top 3 EV Car Brands and Top 3 Hybrid Car Brands in Washington")
    plt.xlabel("Brands")
    plt.ylabel("Amount Sold")
    plt.legend()
    plt.show()