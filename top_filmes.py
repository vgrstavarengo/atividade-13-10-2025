def top_filmes():
    """
    Lê o arquivo de indicados e imprime os filmes ordenados por nota
    (do maior para o menor).
    """
    import os
    
    arquivo = 'filmes_indicacao.txt'
    if not os.path.exists(arquivo):
        print(f"Erro: Arquivo '{arquivo}' não encontrado!")
        print("Execute primeiro a função indicacao()")
        return
    
    arquivo_completo = 'filmes_avaliacao.txt'
    if not os.path.exists(arquivo_completo):
        print(f"Erro: Arquivo '{arquivo_completo}' não encontrado!")
        return
    
    # Ler todas as avaliações
    filmes = []
    with open(arquivo_completo, 'r', encoding='utf-8') as f:
        linhas = f.readlines()
        for linha in linhas[2:]:
            linha = linha.strip()
            if linha:
                partes = linha.split(',', 2)
                if len(partes) == 3:
                    ano = partes[0].strip()
                    titulo = partes[1].strip()
                    nota = float(partes[2].strip())
                    filmes.append({
                        'ano': ano,
                        'titulo': titulo,
                        'nota': nota
                    })
    
    # Ordenar por nota (decrescente)
    filmes.sort(key=lambda x: x['nota'], reverse=True)
    
    # Imprimir ranking
    print(f"\n{'='*60}")
    print("RANKING COMPLETO - DO MELHOR PARA O PIOR")
    print(f"{'='*60}\n")
    
    for i, filme in enumerate(filmes, 1):
        print(f"{i:2d}. [{filme['nota']:4.1f}] {filme['titulo']} ({filme['ano']})")
    
    print(f"\n{'='*60}\n")
