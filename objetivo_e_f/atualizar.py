from utils.atualizar.py import atualizar_formato_cultura1
from utils.atualizar.py import atualizar_formato_cultura2
from utils_dados import CULTURA_1
from utils_dados import CULTURA_2

# Função para atualizar dados de cultura
def atualizar_dados(culturas):
    print("\nEscolha a cultura para atualizar dados:")
    cultura_nome = input(""" 
 0 - VOLTAR AO MENU
 1 - [CULTURA_1]
 2 - [CULTURA_2]
    """).strip().lower()

    if cultura_nome in ('0', 'voltar ao menu', 'voltar'):
        print ("Retornando ao menu principal.")
        return
    if cultura_nome == '1':
        cultura_nome = 'CULTURA_1'
    elif cultura_nome == '2':
        cultura_nome = 'CULTURA_2'
    if cultura_nome not in culturas or not culturas[cultura_nome]:
        print("Cultura não reconhecida ou sem registros. Retornando ao menu inicial.")
        return

    print(f"Você escolheu a {cultura_nome} para atualizar os dados.")
    if cultura_nome == 'CULTURA_1':
        atualizar_formato_cultura1(culturas, cultura_nome)
    elif cultura_nome == 'CULTURA_2':
        atualizar_formato_cultura2(culturas, cultura_nome)
