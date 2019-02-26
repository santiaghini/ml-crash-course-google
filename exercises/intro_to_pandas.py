from __future__ import print_function

import pandas as pd
pd.__version__
import numpy as np

#DataFrames: like relational tables
#Series: one column from the table
#DataFrames consist of one or more Series

#Create a Series
pd.Series(['San Francisco', 'San Jose', 'Sacramento'])

#Create a DataFrame and map column names
city_names = pd.Series(['San Francisco', 'San Jose', 'Sacramento'])
population = pd.Series([852469, 1015785, 485199])

pd.DataFrame({ 'City name': city_names, 'Population': population })

#Load entire csv into a DataFrame
california_housing_dataframe = pd.read_csv("https://download.mlcc.google.com/mledu-datasets/california_housing_train.csv", sep=",")

#Print interesting statistics
california_housing_dataframe.describe()

#Print first items
california_housing_dataframe.head()

#Another powerful feature of pandas is graphing. For example, DataFrame.hist lets you quickly study the distribution of values in a column:
california_housing_dataframe.hist('housing_median_age')

#_______________________________________________________
#ACCESSING DATA

cities = pd.DataFrame({ 'City name': city_names, 'Population': population })
print(type(cities['City name']))
cities['City name']

print(type(cities['City name'][1]))
cities['City name'][1]

print(type(cities[0:2]))
cities[0:2]

#_______________________________________________________
#MANIPULATING DATA

#You may apply Python's basic arithmetic operations to Series. For example:
population / 1000

#NumPy is a popular toolkit for scientific computing. pandas Series can be used as arguments to most NumPy functions:
np.log(population)

#For more complex single-column transformations, you can use Series.apply. Like the Python map function,
# Series.apply accepts as an argument a lambda function, which is applied to each value.
#The example below creates a new Series that indicates whether population is over one million:
overMillion = population.apply(lambda val: val > 1000000)

#Modifying DataFrames is also straightforward. For example, the following code adds two Series to an existing DataFrame:
cities['Area square miles'] = pd.Series([46.87, 176.53, 97.92])
cities['Population density'] = cities['Population'] / cities['Area square miles']
cities

#_______________________________________________________
#EXERCISE #1
#Modify the cities table by adding a new boolean column that is True if and only if both of the following are True:
#The city is named after a saint.
#The city has an area greater than 50 square miles.
#Note: Boolean Series are combined using the bitwise, rather than the traditional boolean, operators. For example, when performing logical and, use & instead of and.
#Hint: "San" in Spanish means "saint."

cities['Is wide and has saint name'] = (cities['Area square miles'] > 50) & cities['City name'].apply(lambda name: name.startswith('San'))
print("Result")
print(cities)

#_______________________________________________________
#INDEXES
#Both Series and DataFrame objects also define an index property that assigns an identifier value to each Series item or DataFrame row.

#By default, at construction, pandas assigns index values that reflect the ordering of the source data. Once created, the index values
# are stable; that is, they do not change when data is reordered.

city_names.index
cities.index

#Call DataFrame.reindex to manually reorder the rows. For example, the following has the same effect as sorting by city name:
cities.reindex([2, 0, 1])

#Reindexing is a great way to shuffle (randomize) a DataFrame. In the example below, we take the index, which is array-like,
# and pass it to NumPy's random.permutation function, which shuffles its values in place. Calling reindex with this shuffled
# array causes the DataFrame rows to be shuffled in the same way. Try running the following cell multiple times!
cities.reindex(np.random.permutation(cities.index))

