def avaliacao():
    """
    Lê o arquivo de filmes, solicita notas de avaliação e salva os resultados.
    """
    import os
    
    # Verificar se o arquivo existe
    arquivo = 'filmes.txt'
    if not os.path.exists(arquivo):
        print(f"Erro: Arquivo '{arquivo}' não encontrado!")
        print("Execute primeiro a função criar_arquivo_filmes()")
        return
    
    # Ler filmes
    filmes = []
    with open(arquivo, 'r', encoding='utf-8') as f:
        for linha in f:
            linha = linha.strip()
            if linha:
                partes = linha.split(',', 1)
                if len(partes) == 2:
                    ano = partes[0].strip()
                    titulo = partes[1].strip()
                    filmes.append({'ano': ano, 'titulo': titulo})
    
    print(f"\n{'='*60}")
    print(f"SISTEMA DE AVALIAÇÃO DE FILMES")
    print(f"{'='*60}\n")
    print(f"Total de filmes: {len(filmes)}\n")
    
    # Solicitar notas
    avaliacoes = []
    for i, filme in enumerate(filmes, 1):
        while True:
            try:
                print(f"{i}. {filme['ano']} - {filme['titulo']}")
                nota = float(input("   Digite a nota (0-10): "))
                
                if 0 <= nota <= 10:
                    avaliacoes.append({
                        'ano': filme['ano'],
                        'titulo': filme['titulo'],
                        'nota': nota
                    })
                    print(f"   ✓ Nota {nota} registrada!\n")
                    break
                else:
                    print("   ⚠ Erro: A nota deve estar entre 0 e 10!\n")
            except ValueError:
                print("   ⚠ Erro: Digite um número válido!\n")
    
    # Salvar avaliações
    with open('filmes_avaliacao.txt', 'w', encoding='utf-8') as f:
        f.write("ANO, TÍTULO, NOTA\n")
        f.write("-" * 60 + "\n")
        for av in avaliacoes:
            f.write(f"{av['ano']}, {av['titulo']}, {av['nota']}\n")
    
    print(f"\n{'='*60}")
    print(f"✓ Avaliações salvas em 'filmes_avaliacao.txt'")
    print(f"{'='*60}\n")