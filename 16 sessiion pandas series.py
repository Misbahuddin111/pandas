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

