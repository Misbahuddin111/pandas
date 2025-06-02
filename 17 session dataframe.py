import numpy as np
import pandas as pd

data = [
    [100,80,10],
    [90,83,8],
    [100,90,8]
]
data_frame = pd.DataFrame(data,columns= ["iq","marks", "pakage"])
print(data_frame)

# dataframe through dictionaries

school_record = {
    "name": ["Misbah", "DAud","Amar","Abdullah"],
    "roll no":[448,456,463,483],
    "skills":["web","Ai","machine learning","devops"]
}

school_data = pd.DataFrame(school_record)
print(school_data)

movies = pd.read_csv("movies.csv")
#print(movies)

ipl = pd.read_csv("ipl-matches.csv")
#print(ipl)

