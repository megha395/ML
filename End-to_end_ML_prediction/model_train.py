from data import *
from sklearn.model_selection import StratifiedShuffleSplit
from sklearn.impute import SimpleImputer

# Preprocessing

# Filling missing values with median
median = data['Horsepower'].median()
data['Horsepower'] = data['Horsepower'].fillna(median)

# Train Test split
split = StratifiedShuffleSplit(n_splits=1, test_size=0.2, random_state=42)

for train_index, test_index in split.split(data, data['Cylinders']):
    train_set = data.loc[train_index]
    test_set = data.loc[test_index]

# # Checking statistic distribution of train set:
# print("statistic distribution of train set")
# print(train_set['Cylinders'].value_counts() / len(train_set))

# # Checking statistic distribution of test set:
# print("statistic distribution of test set")
# print(test_set['Cylinders'].value_counts() / len(test_set))

## Labeling Binary data
## converting integer classes to countries in Origin 
train_set['Origin'] = train_set['Origin'].map({1: 'India', 2: 'USA', 3 : 'Germany'})

## Encoding categorical columns: One hot encoding
train_set = pd.get_dummies(train_set, prefix='', prefix_sep='')

##handling missing values
imputer = SimpleImputer(strategy="median")imputer.fit(num_data)

