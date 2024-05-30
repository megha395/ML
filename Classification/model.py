from Preprocessing import *

### Loading model
model = LogisticRegression()
model.fit(x_train, y_train)

### Prediction of test data
y_pred = model.predict(x_test)
print(f"Predicted data is: \n Test data: \n {x_test} \n Prediction:  \n {y_pred}")
