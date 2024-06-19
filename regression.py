from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.metrics import mean_squared_error, r2_score
import dask.dataframe as dd
import matplotlib.pyplot as plt
import shap
import time

start = time.time()
df = dd.read_csv('out.csv')

df = df.categorize(columns=['Product', 'Repayment Schedule'])
df['Product'] = df['Product'].cat.codes
df['Repayment Schedule'] = df['Repayment Schedule'].cat.codes
df = df.compute()


X = df[['Interest Rate', 'Penalties', 'Product', 'Is Revolving', 'Duration', 'Repayment Schedule', 'Interest Calculation']]
y = df['EOD Processing Time']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = GradientBoostingRegressor(random_state=42)

model.fit(X_train, y_train)

y_pred = model.predict(X_test)

mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"Mean Squared Error: {mse}")
print(f"R-squared: {r2}")

explainer = shap.Explainer(model, X_train)
shap_values = explainer(X_test)

end = time.time()
print(f"Total processing time: {end - start} seconds")

shap.summary_plot(shap_values, X_test, plot_type='bar', show=False)
plt.title('SHAP Feature Importance for Predicting EOD Processing Time')
plt.tight_layout()
plt.savefig('shap_values.png')


