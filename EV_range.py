#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import csv
import matplotlib.pyplot as plt
import random

FILENAME = "Electric_Vehicle_Data.csv"

def read_csv(FILENAME):
    
    """
    Parameters:
    FILENAME: csv file being imported

    Read in a csv file into a list

    Returns: List of data
    """
    
    # Initializing variables
    fin_list = []

    # Opening file
    with open(FILENAME, 'r') as f:
        reader = csv.reader(f)
        
        # Skip header
        next(reader)  

        # Going through every line and adding to list to return
        for line in reader:
            
            # Skip PHEV (Plug-in Hybrid Electric Vehicles)
            if 'PHEV' in line[8]:
                
                continue  
            
            # Skip entries with zero electric range
            elif line[10] == '0':
                
                continue  

            fin_list.append(line)

    return fin_list


def find_average(lst):
    
    """
    Parameters:
    lst: List of data

    Calculate the average electric range from the provided list.

    Returns: Average electric range
    """
    
    sum_range = 0
    count = 0

    # Goes through every row of data to find the average electric range (miles)
    for data in lst:
        
        car_range = data[10] 
        sum_range += float(car_range)
        count += 1

    return round((sum_range / count), 2)


def scatter_plot(lst, avg):
    
    """
    Parameters:
    lst: List of data
    avg: Average electric range

    Create a scatter plot of 150 randomly selected electric vehicles' electric ranges.

    """
    
    electric_ranges = []
    rand_num = random.randint(1, len(lst) - 150)
    count = 0
    count2 = 0

    for data in lst:
        
        count += 1
        
        # Randomized clump of 150 data points taken
        if count >= rand_num:
            
            count2 += 1
            electric_ranges.append(int(data[10]))
            
            # Takes 150 rows
            if count2 == 150:
                break

    # Creating a scatter plot
    plt.scatter(range(len(electric_ranges)), electric_ranges)

    # Adding a horizontal line representing the mean electric range
    plt.axhline(y=avg, color='red', linestyle='--', label='Mean Electric Range of Population (Miles): ' + str(avg))

    # Adding labels, title, and legend
    plt.legend(loc='upper left')
    plt.xlabel('150 Randomly Selected Vehicles')
    plt.ylabel('Electric Range (Miles)')
    plt.title('Sample Electric Vehicles and their Electric Range in Miles')


if __name__ == "__main__":
    
    lst = read_csv(FILENAME)
    
    avg = find_average(lst)
    
    scatter_plot(lst, avg)
    
    
    