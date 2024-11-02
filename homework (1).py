# -*- coding: utf-8 -*-
"""homework.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1sNjtPrmbl9vwuWvWOF4mgAl85kxfu0N_
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
file_path = 'properties_data.csv'
data = pd.read_csv(file_path)

# Selecting relevant features for regression and converting categorical features to dummy variables
data_encoded = pd.get_dummies(data, columns=['neighborhood', 'quality'], drop_first=True)

# Separating features (X) and target variable (price)
X = data_encoded.drop(columns=['id', 'price'])
y = data_encoded['price']

# Splitting the data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Creating and fitting the Random Forest Regression model
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Making predictions
y_pred_train = model.predict(X_train)
y_pred_test = model.predict(X_test)

# Calculating evaluation metrics for training and test sets
metrics = {
    'Train RMSE': np.sqrt(mean_squared_error(y_train, y_pred_train)),
    'Test RMSE': np.sqrt(mean_squared_error(y_test, y_pred_test)),
    'Train MAE': mean_absolute_error(y_train, y_pred_train),
    'Test MAE': mean_absolute_error(y_test, y_pred_test),
    'Train R^2': r2_score(y_train, y_pred_train),
    'Test R^2': r2_score(y_test, y_pred_test)
}

# Display the metrics
print(metrics)

# Plotting predicted price vs. actual price for the test set
plt.figure(figsize=(10, 6))
plt.scatter(y_test, y_pred_test, alpha=0.7)
plt.xlabel('Actual Price')
plt.ylabel('Predicted Price')
plt.title('Actual vs Predicted Price')
plt.plot([y.min(), y.max()], [y.min(), y.max()], 'k--', lw=2)
plt.show()

# Visualizations
# Visualizing relationship between size and price
plt.figure(figsize=(10, 6))
sns.scatterplot(x=data['size_in_sqft'], y=data['price'], alpha=0.7)
plt.xlabel('Size (sqft)')
plt.ylabel('Price')
plt.title('Property Size vs Price')
plt.show()

# Additional visualizations as in the previous code...
# (Repeat the same visualizations as in your original code if needed)