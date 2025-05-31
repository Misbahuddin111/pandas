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