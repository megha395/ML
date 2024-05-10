from data import *
from sklearn.model_selection import StratifiedShuffleSplit


# Preprocessing

# Filling missing values with median
median = data['Horsepower'].median()
data['Horsepower'] = data['Horsepower'].fillna(median)

# Train Test split
split = StratifiedShuffleSplit(n_splits=1, test_size=0.2, random_state=42)
                               

for train_index, test_index in split.split(data, data['Cylinders']):
    train_set = data.loc[train_index]
    test_set = data.loc[test_index]

# Checking statistic distribution of train set:
print(train_set['Cylinders'].value_counts() / len(train_set))