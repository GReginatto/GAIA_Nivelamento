matriz_correlacao = df[colunas_numericas].corr()

correlacoes_com_target = matriz_correlacao['SalePrice'].drop('SalePrice')

correlacoes_ordenadas = correlacoes_com_target.abs().sort_values(ascending=False)


top_corr = correlacoes_ordenadas.head(3).index.tolist() + ['SalePrice']

sns.set(style="whitegrid", context="talk", palette="muted")

plot = sns.pairplot(
    df[top_corr],
    diag_kind='kde',
    corner=True,
    plot_kws={'alpha': 0.6, 's': 50, 'edgecolor': 'k'},
    height=2.8
)

plot.fig.suptitle("Relações entre as Features Mais Correlacionadas", y=1.03, fontsize=16)
plt.tight_layout()
plt.show()
