import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# defining the column names
cols = ['MPG','Cylinders','Displacement','Horsepower','Weight',
                'Acceleration', 'Model Year', 'Origin']

# reading the data using pandas
df = pd.read_csv("auto-mpg.data", 
                 names=cols, 
                 na_values = "?",
                 comment = '\t',
                 sep= " ",
                 skipinitialspace=True)

# print(df)

#making a copy of the dataframe
data = df.copy()