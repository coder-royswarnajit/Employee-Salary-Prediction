import pandas as pd
import os
import kagglehub

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error

import joblib
import matplotlib.pyplot as plt

path = kagglehub.dataset_download("abdallahwagih/company-employees")
path = os.path.join(path, "employees.xlsx")
data=pd.read_excel(path)


#Cleaning the data
data.dropna(inplace=True)
data.drop_duplicates(inplace=True)

#Model Training
X=data[["Years","Job Rate"]]
Y=data["Annual Salary"]

X_train,X_test, Y_train, Y_test = train_test_split(X,Y,test_size=0.2)

lr=LinearRegression()
lr.fit(X_train,Y_train)

predslr=lr.predict(X_test)

mean_absolute_error(predslr,Y_test)

joblib.dump(lr,"linearmodel.pkl")

# Plot Years vs Annual Salary
plt.figure(figsize=(8, 5))
plt.scatter(data["Years"], data["Annual Salary"], alpha=0.6)
plt.xlabel("Years at Company")
plt.ylabel("Annual Salary")
plt.title("Years at Company vs Annual Salary")
plt.grid(True, linestyle='--', alpha=0.5)
plt.tight_layout()
plt.savefig("years_vs_salary.png")
plt.show()