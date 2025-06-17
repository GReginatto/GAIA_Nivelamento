
Q1 = df[colunas_numericas].quantile(0.25)
Q3 = df[colunas_numericas].quantile(0.75)
IQR = Q3 - Q1

outliers = (df[colunas_numericas] < (Q1 - 1.5 * IQR)) | (df[colunas_numericas] > (Q3 + 1.5 * IQR))

for coluna in colunas_numericas:
    print('---', coluna, '---')
    print('Q1  =', Q1[coluna])
    print('Q3  =', Q3[coluna])
    print('IQR =', IQR[coluna])
    print('Outliers =', outliers[coluna].sum())

    plt.figure(figsize=(8, 4))
    sns.boxplot(y=df[coluna], width=0.3, color='skyblue')
    plt.title(f"Boxplot de {coluna}")
    plt.tight_layout()
    plt.show()
