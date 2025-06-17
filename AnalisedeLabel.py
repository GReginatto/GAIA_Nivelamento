for coluna in colunas_categoricas:
    print(f"\n Analisando coluna categórica: {coluna}")

    contagem = df[coluna].value_counts(dropna=False)
    proporcao = df[coluna].value_counts(normalize=True, dropna=False)

    print("Contagem:")
    print(contagem)
    print("\nProporção:")
    print(proporcao)

    if contagem.shape[0] <= 5:
        #Gráfico de pizza
        plt.figure(figsize=(6, 6))
        contagem.plot.pie(
            autopct='%1.1f%%',
            startangle=90,
            colors=sns.color_palette("Set2"),
            wedgeprops={'edgecolor': 'black'}
        )
        plt.ylabel('')
        plt.title(f'Proporção das classes: {coluna}')
        plt.tight_layout()
        plt.show()

    else:
        # Gráfico de barras horizontal
        plt.figure(figsize=(8, 6))
        sns.countplot(data=df, y=coluna, order=contagem.index, palette="Set3")
        plt.title(f'Distribuição da coluna: {coluna}')
        plt.xlabel("Contagem")
        plt.ylabel("Classe")
        plt.grid(axis='x')
        plt.tight_layout()
        plt.show()


coluna = input("Digite o nome da coluna para analisar: ")

if coluna not in df.columns:
    print(f"Coluna '{coluna}' não encontrada no DataFrame.")
else:
    contagem = df[coluna].value_counts(dropna=False)

    if contagem.shape[0] <= 5:
        # Gráfico de pizza
        plt.figure(figsize=(6, 6))
        contagem.plot.pie(
            autopct='%1.1f%%',
            startangle=90,
            colors=sns.color_palette("Set2"),
            wedgeprops={'edgecolor': 'black'}
        )
        plt.ylabel('')
        plt.title(f'Proporção das classes: {coluna}')
        plt.tight_layout()
        plt.show()
    else:
        # Gráfico de barras horizontal
        plt.figure(figsize=(8, 6))
        sns.countplot(data=df, y=coluna, order=contagem.index, palette="Set3")
        plt.title(f'Distribuição da coluna: {coluna}')
        plt.xlabel("Contagem")
        plt.ylabel("Classe")
        plt.grid(axis='x')
        plt.tight_layout()
        plt.show()
