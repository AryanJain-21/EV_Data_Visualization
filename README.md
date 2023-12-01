# EV Data Visualization


## Academic Project that runs 3 main functions: Data Visualization and Analysis functions. Uses data pulled from Kaggle, 150k+ rows, which describes electric and hybrid vehicles registered in the state of Washington. 

The first function, EV_models, analyzes the brands and models of the registered cars, showing the differences between sold electric and hybrid vehicles. This information is presented visually using Matplotlib in the form of bar graphs. 

The second function, EV_heatmap, analyzes the population density of registered cars in Washington. Imports a dictionary containing all the cities in Washington and their latitudes and longitudes and uses that to create a data frame in the format required by Density Mapbox (a tool from Plotly Express). A heatmap is created using Plotly Express to show population density. A scatter plot is also put onto the usual heatmap to display smaller populations. 
  A .py and .ipynb file are provided, both coded differently but very similarly.

The third function, EV_range, is analyzing the electric range (miles) of electric vehicles. First, clean null values and remove hybrid vehicles, which have a significantly lower electric range and skew data. The mean electric range of the entire population is found, but the information is visualized, using Matplotlib, on a scatterplot using a sample of the population to have a clearer visual. A random clump of 150 vehicles is used for the scatterplot, and the mean is also plotted.


## In the future

Increasing the scope of the project by using data from registered vehicles outside of the state of Washington. Cleaning up code, making it more efficient, and using more tools to visualize the functions. 

## How to Install and Run the project

Download the Kaggle Data (Linked below), Electric_Vehicle_Data.csv, to run all the functions. 

For the heatmap, install washington_cities.py to import the latitudes and longitudes of cities. 
Install Plotly Express: !pip install plotly_express==0.4.0

## Credits

[https://catalog.data.gov/dataset/electric-vehicle-population-data](url)

[https://towardsdatascience.com/creating-geospatial-heatmaps-with-pythons-plotly-and-folium-libraries-4159e98a1ae8#:~:text=To%20do%20this%2C%20we%20first,the%20data%20point%2C%20and%20more.](url)


## License

MIT License
