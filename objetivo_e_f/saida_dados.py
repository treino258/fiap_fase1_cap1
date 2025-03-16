from utils_dados.py import cultura1
from utils_dados.py import cultura2

# Função para saída de dados
def saida_dados(culturas):
    print("\nSaída de Dados:")
    cultura_nome = input("""
 0 - VOLTAR AO MENU
 1 - cultura1
 2 - cultura2
    """).strip().lower()
    
    if cultura_nome == '0' or cultura_nome == 'voltar ao menu':
        return
    if cultura_nome not in {'1', 'cultura1', '2', 'cultura2'}:
        print("Cultura não reconhecida. Retornando ao menu.")
        return
    if cultura_nome in {'1', 'cultura1'}:
        cultura_nome = 'cultura1'
    elif cultura_nome in {'2', 'cultura2'}:
        cultura_nome = 'cultura2'
    
    print(f"\nDados para {cultura_nome}:")
    if not culturas[cultura_nome]:
        print("Nenhum dado registrado.")
    else:
        for i, dado in enumerate(culturas[cultura_nome], 1):
            print(f"  Registro {i}: Área = {dado['area']} m², Insumo = {dado['manejo']} mL")
