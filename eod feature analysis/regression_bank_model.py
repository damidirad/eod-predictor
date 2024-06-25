import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from xgboost import XGBRegressor
import matplotlib.pyplot as plt
import shap
import time
import joblib
import pandas as pd

start_time = time.time()

# Load data
bank_data = pd.read_csv('bank.csv')
# bank_data = pd.read_csv('processing_time.csv')
#bank_data = df.merge(bank_df, on='BANK')

# Prepare data and column to predict
X = bank_data.drop(columns=['BANK', 'ACCOUNTHOLDERKEY', 'ACCOUNTLOANPROCESSINGTIME'])
y = bank_data['ACCOUNTLOANPROCESSINGTIME']

# Create preprocessor
categorical_features = ['SCHEDULEDUEDATESMETHOD', 'INTERESTCALCULATIONMETHOD', 'PRODUCTNAME']
numeric_features = X.columns.difference(categorical_features)

preprocessor = ColumnTransformer(
    transformers=[
        ('num', StandardScaler(), numeric_features),
        ('cat', OneHotEncoder(), categorical_features)
    ])

# Train test split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create pipeline
model = Pipeline(steps=[('preprocessor', preprocessor),
                        ('regressor', XGBRegressor(random_state=42))])

print(f"Model ready to be trained")
model.fit(X_train, y_train)
print(f"Model successfully trained in {time.time() - start_time} seconds")

# Save the trained model
joblib.dump(model, "100_banks_8_products_xgboost_.pkl")

# Make predictions
y_pred = model.predict(X_test)

# Evaluate the model
print('Mean Squared Error:', mean_squared_error(y_test, y_pred))
print('R^2 Score:', r2_score(y_test, y_pred))

start_time = time.time()

print(f"Starting SHAP analysis")
X_test_transformed = model.named_steps['preprocessor'].transform(X_test)

# Use SHAP to explain the model predictions
explainer = shap.Explainer(model.named_steps['regressor'])
shap_values = explainer(X_test_transformed)

shap.summary_plot(shap_values, 
                  X_test_transformed, 
                  plot_size=[10,6], 
                  feature_names=model.named_steps['preprocessor'].get_feature_names_out(), 
                  show=False)
plt.savefig("shap_summary_plot.png")

# Feature importance plot
shap.summary_plot(shap_values, 
                  X_test_transformed, 
                  feature_names=model.named_steps['preprocessor'].get_feature_names_out(), 
                  plot_type="bar")
plt.savefig("shap_importance_plot.png")

print(f"SHAP analysis succesful after {time.time() - start_time} seconds")