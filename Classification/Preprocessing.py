# importing libraries
from Global_imports import *

data = pd.read_csv("loan.csv")
# print(data.head(5))

lr = LabelEncoder()
for i in data.columns:
    if data[i].dtypes == 'object':
        data[i]= lr.fit_transform(data[i])

## Separating dependent and independent features
X = data.drop(['loan_status'], axis = 1)
Y = data['loan_status']

### Train test split
x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=0.30, random_state=42)

## Standardization of data
scale = StandardScaler()
x_train = scale.fit_transform(x_train)
x_test = scale.transform(x_test)

print('x_train size:', x_train.shape)
print('x_test size:', x_test.shape)
print('y_train size:', y_train.shape)
print('y_test size:', y_test.shape)
