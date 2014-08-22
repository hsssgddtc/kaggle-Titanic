import pandas as pd
import numpy as np
import pylab as p
from sklearn.ensemble import RandomForestClassifier 

df = pd.read_csv('../data/train.csv',header=0)

df["Gender"] = df["Sex"].map( lambda x: x[0].upper())
df["Gender"] = df["Sex"].map({"female": 0, "male": 1}).astype(int)
df["Location"] = df["Embarked"].map({"S": 0, "C":1, "Q":2})

median_ages = np.zeros((2,3))
for i in range(0,2):
    for j in range(0,3):
        median_ages[i, j] = df[(df["Gender"]==i) & (df["Pclass"]==j+1)]["Age"].dropna().median()

df["AgeFill"] = df["Age"]
for i in range(0,2):
    for j in range(0,3):
        df.loc[ (df.Age.isnull()) & (df.Gender==i) & (df.Pclass==j+1), "AgeFill"] = median_ages[i, j]
#df["AgeIsNull"] = pd.isnull(df.Age).astype(int)
#df["FamilySize"] = df["SibSp"] + df["Parch"]
#df["Age*Class"] = df.AgeFill * df.Pclass

df = df.drop(["PassengerId","Age","Name","Sex","Ticket","Cabin","Embarked"], axis=1)
#print df.head(3)
#print df.dtypes[df.dtypes.map(lambda x: x=="object")]

train_data = df.values
print train_data

forest = RandomForestClassifier(n_estimators = 100)
forest = forest.fit(train_data[0::,1::], train_data[0::, 0])

#output = forest.predict(test_data)
#print df[df["Age"].isnull()][["Gender","Pclass","Age","AgeFill","AgeIsNull"]].head(10)
#print df.describe()
 