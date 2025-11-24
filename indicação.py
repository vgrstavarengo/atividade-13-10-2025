def indicacao():
    """
    Lê o arquivo de avaliações, seleciona os 5 filmes com maiores notas
    e salva em ordem alfabética.
    """
    import os
    
    arquivo = 'filmes_avaliacao.txt'
    if not os.path.exists(arquivo):
        print(f"Erro: Arquivo '{arquivo}' não encontrado!")
        print("Execute primeiro a função avaliacao()")
        return
    
    # Ler avaliações
    filmes = []
    with open(arquivo, 'r', encoding='utf-8') as f:
        linhas = f.readlines()
        for linha in linhas[2:]:  # Pula cabeçalho
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
    
    # Selecionar top 5
    top5 = filmes[:5]
    
    # Ordenar alfabeticamente
    top5.sort(key=lambda x: x['titulo'])
    
    # Salvar indicados
    with open('filmes_indicacao.txt', 'w', encoding='utf-8') as f:
        f.write("TOP 5 FILMES INDICADOS (Ordem Alfabética)\n")
        f.write("=" * 60 + "\n\n")
        for i, filme in enumerate(top5, 1):
            f.write(f"{i}. {filme['titulo']} ({filme['ano']}) - Nota: {filme['nota']}\n")
    
    print(f"\n{'='*60}")
    print("TOP 5 FILMES INDICADOS")
    print(f"{'='*60}\n")
    for i, filme in enumerate(top5, 1):
        print(f"{i}. {filme['titulo']} ({filme['ano']}) - Nota: {filme['nota']}")
    
    print(f"\n{'='*60}")
    print("✓ Lista salva em 'filmes_indicacao.txt'")
    print(f"{'='*60}\n")