import pandas as pd
from sklearn.linear_model import Ridge
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
import joblib

data = pd.read_csv('car_prices.csv')

X = data.drop('Price', axis=1)
y = data['Price']

categorical = ['Make', 'FuelType', 'Transmission']
numerical = ['Year', 'Mileage', 'OwnerCount']



preprocessor = ColumnTransformer([
    ('cat', OneHotEncoder(), categorical),
    ('num', StandardScaler(), numerical)
])


pipeline = Pipeline([
    ('preprocessor', preprocessor),
    ('ridge', Ridge(alpha=1.0))
])

pipeline.fit(X, y)


joblib.dump(pipeline, 'model/ridge_model.pkl')

print(" Ridge Regression model saved to model/ridge_model.pkl")
