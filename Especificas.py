#  Distribuição da variável alvo SalePrice


plt.figure(figsize=(8,5))
sns.histplot(df['SalePrice'], kde=True, bins=30, color='lightgreen')
plt.title("Distribuição de SalePrice")
plt.xlabel("SalePrice")
plt.ylabel("Frequência")
plt.grid(True)
plt.tight_layout()
plt.show()

# Analise de válores nulos

valores_nulos = df.isnull().sum()
valores_nulos = valores_nulos[valores_nulos > 0].sort_values(ascending=False)

plt.figure(figsize=(10,6))
sns.barplot(x=valores_nulos.values, y=valores_nulos.index, palette="Reds_r")
plt.title("Valores Nulos por Coluna")
plt.xlabel("Total de Nulos")
plt.ylabel("Coluna")
plt.tight_layout()
plt.show()

# Scatter plot entre features mais correlacionadas e SalePrice

top_features = correlacoes_ordenadas.head(3).index.tolist()

for feature in top_features:
    plt.figure(figsize=(7, 4))

    sns.scatterplot(x=df[feature], y=df['SalePrice'], alpha=0.5, color='blue', label='Outros')

    idx_max = df['SalePrice'].idxmax()
    plt.scatter(df.loc[idx_max, feature], df.loc[idx_max, 'SalePrice'],
                color='red', s=80, label='Maior SalePrice')

    plt.title(f"{feature} vs SalePrice")
    plt.xlabel(feature)
    plt.ylabel("SalePrice")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()
