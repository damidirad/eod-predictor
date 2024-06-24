import joblib
import pandas as pd
import shap
from sklearn.model_selection import train_test_split

# Load the trained model
model = joblib.load('100_banks_8_products.pkl')

# Load the data
df = pd.read_csv('bank.csv')
bank_df = pd.read_csv('processing_time.csv')

# Merge loan processing time data with bank data
bank_data = df.merge(bank_df, on='BANK')

# Prepare the features and target variable
X = bank_data.drop(columns=['BANK', 'ACCOUNTHOLDERKEY', 'LOANPROCESSINGTIME'])
y = bank_data['LOANPROCESSINGTIME']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Transform the test data using the pipeline's preprocessor
X_test_transformed = model.named_steps['preprocessor'].transform(X_test)

# Use SHAP to explain the model's predictions
explainer = shap.Explainer(model.named_steps['regressor'])
shap_values = explainer(X_test_transformed)

# Summary plot
shap.summary_plot(shap_values, X_test_transformed, feature_names=model.named_steps['preprocessor'].get_feature_names_out())

# Feature importance plot
shap.summary_plot(shap_values, X_test_transformed, feature_names=model.named_steps['preprocessor'].get_feature_names_out(), plot_type="bar")
