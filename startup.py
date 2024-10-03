import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import OneHotEncoder
from sklearn.metrics import mean_absolute_error,mean_squared_error, r2_score

startups_df = pd.read_csv('50_Startups.csv')
startups_df.head()

startups_df.info()
startups_df.describe()
startups_df.shape

startups_df.corr()
sns.heatmap(startups_df.corr(), annot=True)

# SPLITTING THE DATA INTO INDEPEDENT AND DEPENDENT VARIABLES(X, y)
X = startups_df.iloc[:, :-1]    # Independent varibles
y = startups_df.iloc[:, -1]     # dependent variable

#-----------------------------------------------------------------------------------------------------
#In Order to Complete this regression Code You can you werite the OneHotEncoder Part Over here 

# USING OneHotEncoder TO CONVERT CATEGORICAL DATA TO DUMMY VARIABLES
# For now Convert the ['Florida', 'New York'] into one-hot-encoded values 
# And make X = X.join(encoded_df) where encoded_df is the encoded values data_value



#----------------->DO-NOT-EDIT THIS SECTION<-----------------------------
# SPLITTING DATA FOR train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# FITTING THE MODEL/TRAIN
regressor = LinearRegression() 
regressor.fit(X_train, y_train)

print('Coefficients: ', regressor.coef_)
print('Intercept: ',regressor.intercept_)

# PREDICTING
y_pred=regressor.predict(X_test)
# predictions
comparison_df = pd.DataFrame({"Actual":y_test,"Predicted":y_pred})
print(comparison_df)

# RESIDUALS
residuals = y_test - y_pred
print('Residuals: ', residuals)

# CHECKING THE SCORE OF THE MODEL WITH R^2 METRIC
score = r2_score(y_test, y_pred)
print('Model Score: ', score, 'Equal to: ', score * 100, '%')