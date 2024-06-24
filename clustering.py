import dask.dataframe as dd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import seaborn as sns
import time

start_time = time.time()

df = dd.read_csv('out.csv')

df = df.categorize(columns=['Product', 'Repayment Schedule'])
df['Product'] = df['Product'].cat.codes
df['Repayment Schedule'] = df['Repayment Schedule'].cat.codes
df = df.compute()


features = df[['Interest Rate', 'Penalties', 'Product', 'Is Revolving', 'EOD Processing Time', 'Term', 'Repayment Schedule', 'Interest Calculation']]

n_clusters = 3
kmeans = KMeans(n_clusters=n_clusters, random_state=42)

subset = features[:100000] 
kmeans.fit(subset)

df['Cluster'] = kmeans.predict(features)

# Perform PCA to reduce the dimensions to 2D for visualization
pca = PCA(n_components=3)
features_pca = pca.fit_transform(features)


df['PCA1'] = features_pca[:, 0]
df['PCA2'] = features_pca[:, 1]
df['PCA3'] = features_pca[:, 2]

end_time = time.time()

print(f"Total processing time: {end_time - start_time} seconds")

sample_df = df.sample(frac=0.1, random_state=42) 

# Plot in 3D
fig = plt.figure(figsize=(12, 10))
ax = fig.add_subplot(111, projection='3d')

scatter = ax.scatter(sample_df['PCA1'], sample_df['PCA2'], sample_df['PCA3'], c=sample_df['Cluster'], cmap='viridis', s=50)
ax.set_title('Loan Data Clustering')
ax.set_xlabel('PCA Component 1')
ax.set_ylabel('PCA Component 2')
ax.set_zlabel('PCA Component 3')

# Adding a color bar
plt.colorbar(scatter, ax=ax, label='Cluster')
plt.savefig('bank_clusters.png')