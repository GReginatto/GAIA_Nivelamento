faltantes_total = df.isnull().sum()
faltantes_percentual = (faltantes_total / len(df)) * 100

dados_faltantes = pd.DataFrame({
    'Total': faltantes_total,
    'Porcentagem': faltantes_percentual
}).query("Total > 0").sort_values('Porcentagem', ascending=False)

plt.figure(figsize=(10, 6))
sns.barplot(
    x=dados_faltantes['Porcentagem'],
    y=dados_faltantes.index,
    palette="Reds_r"
)

for i, v in enumerate(dados_faltantes['Porcentagem']):
    plt.text(v + 1, i, f"{v:.1f}%", va='center')

plt.title("Dados Faltantes por Coluna", fontsize=14)
plt.xlabel("Porcentagem de Dados Faltantes")
plt.ylabel("Colunas")
plt.grid(axis='x', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

print(dados_faltantes)
