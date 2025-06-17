matriz_correlacao = df[colunas_numericas].corr()

plt.figure(figsize=(16, 14))
sns.heatmap(matriz_correlacao, annot=True, cmap='coolwarm', fmt=".2f", annot_kws={"size": 8})
plt.xticks(rotation=90, fontsize=8)
plt.yticks(fontsize=8)
plt.title("Matriz de Correlação", fontsize=16, pad=20)
plt.tight_layout()
plt.show()

correlacoes_com_target = matriz_correlacao['SalePrice'].drop('SalePrice')
correlacoes_ordenadas = correlacoes_com_target.abs().sort_values(ascending=False)

print("Features mais correlacionadas com SalePrice:")
print(correlacoes_ordenadas)
