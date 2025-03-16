from utils.dados.py import cultura1
from utils.dados.py import cultura2

# Função para deletar um dado específico dentro de cada cultura
def deletar_formato_cultura(culturas, cultura_nome):
    print("\nEscolha o registro para deletar:")
    if not culturas[cultura_nome]:
        print("Nenhum dado registrado.")
    else:
        for i, dado in enumerate(culturas[cultura_nome], 1):
            print(f"  Registro {i}: Área = {dado['area']} m², Insumo = {dado['manejo']} mL")
    
    # Solicita o índice antes de confirmar
    indice = int(input(f"Pressione 0 para voltar ao menu. Digite o índice do registro a ser deletado (1 a {len(culturas[cultura_nome])}): "))
    
    if indice == 0:
        print("Retornando ao menu principal.")
        return

    if indice < 1 or indice > len(culturas[cultura_nome]):
        print("Índice inválido.")
        return
    
    print(f"Você escolheu deletar o registro {indice}. Tem certeza?")
    confirmacao = input("""
    0 - NÃO
    1 - SIM
    """).strip().lower()
    
    # Verificação de confirmação
    if confirmacao in ('0', 'não', 'nao', 'n', 'no', 'NÃO', 'NAO', 'N', 'NO'):
        print("Operação cancelada. Retornando ao menu.")
        return  # Cancela a operação
    elif confirmacao == '1' or confirmacao == 'sim':
        culturas[cultura_nome].pop(indice - 1)
        print(f"Registro {indice} deletado com sucesso.")
