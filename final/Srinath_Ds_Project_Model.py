import numpy as np
import matplotlib.pyplot as pt
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.svm import LinearSVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
import joblib


data = pd.read_csv("Downloads/train.csv")
print("made data")
print("")
features  = data.drop("label", axis = 1)
target = data["label"]
X_train, X_test, y_train, y_test = train_test_split(features, target, random_state=3000)
print("made training and test data")
print("")

knn = KNeighborsClassifier(n_neighbors = 6)

k1 = KNeighborsClassifier(n_neighbors = 4)

model = DecisionTreeClassifier(max_depth = 10)

gnb = GaussianNB()

print("made models")
print("")

knn.fit(X=X_train, y=y_train)
filename = 'Downloads/knn_model.sav'
joblib.dump(knn, filename)
print("fit KNeighborsClassifier")
print("")
print("saved the trained knn model")
print("")

#k1.fit(X=X_train, y=y_train)

model.fit(X=X_train, y=y_train)
print("fit DecisionTreeClassifier")
print("")

gnb.fit(X=X_train, y=y_train)
print("fit GaussianNB")
print("")

print("calculating accuracies:")
print("")

print("Prediction accuracy on the training data with KNeighborsClassifier :", format(knn.score(X_train, y_train)*100, ".2f"))
print("Prediction accuracy on the test data with KNeighborsClassifier :", format(knn.score(X_test, y_test)*100, ".2f"))
print("")

print("Prediction accuracy on the training data with DecisionTreeClassifier :", format(model.score(X_train, y_train)*100, ".2f"))
print("Prediction accuracy on the test data with DecisionTreeClassifier :", format(model.score(X_test, y_test)*100, ".2f"))
print("")

print("Prediction accuracy on the training data with GaussianNB :", format(gnb.score(X_train, y_train)*100, ".2f"))
print("Prediction accuracy on the test data with GaussianNB :", format(gnb.score(X_test, y_test)*100, ".2f"))
print("")

# print("Prediction accuracy on the training data with k1 :", format(k1.score(X_train, y_train)*100, ".2f"))
# print("Prediction accuracy on the test data with k1 :", format(k1.score(X_test, y_test)*100, ".2f"))
# print("")

print("testing the model with singular data")
print("")
loaded_model = joblib.load("Downloads/knn_model.sav")
#indexes start from 14322 and has 10,500 numbers for test data. 
#indexes for eg are: 14322, 22264, 32118 etc.
# use same number for index in x_test  and y_test: y_test  are the  answers  for x_test.
d = X_test.loc[[21284]]
print(y_test[21284])
print("")
print(loaded_model.predict(X_test.loc[[21284]])[0])
print("")

if(y_test[21284] == loaded_model.predict(X_test.loc[[21284]])[0]):
    print("test passed")
else:
    print("test failed")
