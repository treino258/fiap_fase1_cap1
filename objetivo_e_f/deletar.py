from utils_deletar.py import deletar_formato_cultura
from utils_dados import CULTURA_1
from utils_dados import CULTURA_2

# Função para deletar dados
def deletar_dados(culturas):
    print("\nEscolha a cultura para deletar dados:")
    cultura_nome = input(""" 
 0 - VOLTAR AO MENU
 1 - cultura1
 2 - cultura2
    """).strip().lower()
    
    # Mapeia as escolhas para as chaves do dicionário
    if cultura_nome == '0' or cultura_nome == 'voltar ao menu':
        return
    if cultura_nome == '1':
        cultura_nome = 'cultura1'
    elif cultura_nome == '2':
        cultura_nome = 'cultura2'
    
    if cultura_nome not in culturas or not culturas[cultura_nome]:
        print("Cultura não reconhecida ou sem registros. Retornando ao menu.")
        return
    
    print(f"Você escolheu a {cultura_nome} para deletar os dados.")
    if cultura_nome == 'cultura1':
        deletar_formato_cultura(culturas, 'cultura1')
    elif cultura_nome == 'cultura2':
        deletar_formato_cultura(culturas, 'cultura2')