def estatisticas_descritivas(dados, nome_coluna="Variável"):
    dados.sort()

    media = sum(dados) / len(dados)
    soma_dos_quadrados = sum((x - media) ** 2 for x in dados)
    variancia = soma_dos_quadrados / len(dados)
    desvio_padrao = math.sqrt(variancia)

    n = len(dados)
    if n % 2 == 0:
        mediana = (dados[n//2 - 1] + dados[n//2]) / 2
    else:
        mediana = dados[n//2]

    maior = max(dados)
    menor = min(dados)

    print(f"\n Estatísticas para {nome_coluna}")
    print(f"Média: {media:.2f}")
    print(f"Mediana: {mediana:.2f}")
    print(f"Desvio Padrão: {desvio_padrao:.2f}")
    print(f"Maior Valor: {maior}")
    print(f"Menor Valor: {menor}")

    plt.figure(figsize=(8, 5))
    sns.histplot(dados, kde=True, color="skyblue", bins=30)

    plt.axvline(media, color='red', linestyle='--', label=f'Média: {media:.2f}')
    plt.axvline(mediana, color='green', linestyle='-.', label=f'Mediana: {mediana:.2f}')
    plt.axvline(media + desvio_padrao, color='orange', linestyle=':', label=f'Média + σ: {(media + desvio_padrao):.2f}')
    plt.axvline(media - desvio_padrao, color='orange', linestyle=':', label=f'Média - σ: {(media - desvio_padrao):.2f}')

    plt.title(f"Distribuição de {nome_coluna}")
    plt.xlabel(nome_coluna)
    plt.ylabel("Frequência")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

for coluna in colunas_numericas:
    print(f"\nAnalisando coluna: {coluna}")
    dados = df[coluna].dropna().tolist()
    estatisticas_descritivas(dados, nome_coluna=coluna)
