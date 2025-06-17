from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

features_cluster = ['GrLivArea', 'GarageCars', 'SalePrice']

df_cluster = df[features_cluster].dropna()

scaler = StandardScaler()
dados_normalizados = scaler.fit_transform(df_cluster)

kmeans = KMeans(n_clusters=3, random_state=42)
df_cluster['Cluster'] = kmeans.fit_predict(dados_normalizados)

plt.figure(figsize=(10, 6))
sns.scatterplot(
    data=df_cluster,
    x='GrLivArea',
    y='SalePrice',
    hue='Cluster',
    palette='Set2',
    alpha=0.7
)
plt.title("Clusterização KMeans: GrLivArea x SalePrice")
plt.xlabel("GrLivArea (Área útil)")
plt.ylabel("SalePrice (Preço de venda)")
plt.grid(True)
plt.tight_layout()
plt.show()
