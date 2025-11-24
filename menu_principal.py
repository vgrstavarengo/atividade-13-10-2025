def menu():
    """Menu interativo para executar todas as funcionalidades"""
    while True:
        print(f"\n{'='*60}")
        print("SISTEMA DE AVALIAÇÃO DE FILMES")
        print(f"{'='*60}")
        print("\n1. Criar arquivo de filmes (filmes.txt)")
        print("2. Avaliar filmes (avaliacao.py)")
        print("3. Indicar Top 5 (indicacao.py)")
        print("4. Ver ranking completo (top_filmes.py)")
        print("5. Executar tudo em sequência")
        print("0. Sair")
        print(f"\n{'='*60}")
        
        opcao = input("\nEscolha uma opção: ").strip()
        
        if opcao == '1':
            criar_arquivo_filmes()
        elif opcao == '2':
            avaliacao()
        elif opcao == '3':
            indicacao()
        elif opcao == '4':
            top_filmes()
        elif opcao == '5':
            print("\nExecutando todas as etapas...\n")
            criar_arquivo_filmes()
            input("\nPressione Enter para continuar com as avaliações...")
            avaliacao()
            indicacao()
            top_filmes()
        elif opcao == '0':
            print("\nSaindo... Até logo! \n")
            break
        else:
            print("\n⚠ Opção inválida! Tente novamente.")
