import numpy as np
import pandas as pd

# string
names = ["misbah","amar","daud","abdullah","yasir"]
print(pd.Series(names))

# integers
numbers = [23,42,54,64,67,32]
print(pd.Series(numbers))

# custom indexing
marks = [55,64,74,46,75]
subjects = ["maths","urdu","english","physics","computer"]
print(pd.Series(marks , index=subjects, name="Report card"))

# series in dict 
data = {
    "name": "misbah",
    "semester": "7th",
    "roll no": 448,
    "Department": "IBMS",
}
data_series = pd.Series(data ,name= "misbah data")
print(data_series)

# series attributes

# size 
print("size :",data_series.size)

#dtype
print(f"dtype : {data_series.dtype}")
# name
print(f"name : {data_series.name}")
# is_unique
print(f"is_unique : {data_series.is_unique}")
# index 
print(f"index : {data_series.index}")

# value 
print(f"values : {data_series.values}")

import pandas as pd

# Read the CSV into a DataFrame
subs = pd.read_csv('subs.csv')

# Convert single-column DataFrame to Series
subs = subs.squeeze()
print(subs)
print(type(subs))  # Should show <class 'pandas.core.series.Series'>


#with two columns
vk = pd.read_csv('kohli_ipl.csv', index_col="match_no")
vks = vk.squeeze()
print(vks)
print(type(vks))

movies = pd.read_csv('bollywood.csv',index_col="movie")
tyop = movies.squeeze()
print(type(tyop))


# series methods 
# head method
print(movies.head(3))

# tail method
print(movies.tail(2))

# sample method  ( generate random items from file)

print(subs.sample())

# values count (The .value_counts() method in Pandas counts unique values in a Series,)
print(vk.value_counts())

# sort_value
print(vks.sort_values(ascending=False).head(1).values[0])


# sort_index
print(movies.sort_index(ascending=False))

# series maths method
# counnt method
print(subs.count())

#sum 
print(subs.sum())
# mean
subs.mean()
# median
print(vk.median())

#mode
print(movies.mode())
# std
print(subs.std())
# var
print(vk.var())

# min/max

print(vks.min())
print(vks.max())

# describe 
print(subs.describe())

print(subs.plot())
