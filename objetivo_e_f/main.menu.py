from entrada.dados.py import entrada_dados # Importando a função de entrada de dados
from saida.dados.py import saida_dados # Importando a função de saída de dados
from atualizar.py import atualizar_dados # Importando a função de atualização de dados
from deletar.py import deletar_dados # Importando a função de deleção de dados

# Função para exibir o menu
def exibir_menu():
    print("\nMenu de Opções:")
    print("1 - Entrada de Dados")
    print("2 - Saída de Dados")
    print("3 - Atualizar Dados")
    print("4 - Deletar Dados")
    print("0 - Sair do Programa")

# Função principal para gerenciar o menu
def main():

    while True:
        exibir_menu()
        escolha = input("Escolha uma opção (1-4 ou 'Sair'): ").strip().lower()

        if escolha in {'1', 'entrada','Entrada de Dados', 'entrada de dados', 'entrar'}:
            entrada_dados(culturas)
        elif escolha in {'2', 'saída','saida de dados', 'Saída de Dados'}:
            saida_dados(culturas)
        elif escolha in {'3', 'atualizar', 'atualizar dados'}:
            atualizar_dados(culturas)
        elif escolha in {'4', 'deletar', 'deletar dados'}:
            deletar_dados(culturas)
        elif escolha in {'0', 'sair', 'sair do programa', 'fechar'}:
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida. Tente novamente.")

# Executando o programa
if __name__ == "__main__":
    main()
