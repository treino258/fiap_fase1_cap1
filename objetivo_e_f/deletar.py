from utils.deletar.py import deletar_formato_cultura
from utils.dados.py import cultura1
from utils.dados.py import cultura2

# Função para atualizar dados de cultura
def atualizar_dados(culturas):
    print("\nEscolha a cultura para atualizar dados:")
    cultura_nome = input(""" 
 0 - VOLTAR AO MENU
 1 - cultura1
 2 - cultura2
    """).strip().lower()

    if cultura_nome in ('0', 'voltar ao menu', 'voltar'):
        print ("Retornando ao menu principal.")
        return
    if cultura_nome == '1':
        cultura_nome = 'cultura1'
    elif cultura_nome == '2':
        cultura_nome = 'cultura2'
    if cultura_nome not in culturas or not culturas[cultura_nome]:
        print("Cultura não reconhecida ou sem registros. Retornando ao menu inicial.")
        return

    print(f"Você escolheu a {cultura_nome} para atualizar os dados.")
    if cultura_nome == 'cultura1':
        atualizar_formato_cultura1(culturas, cultura_nome)
    elif cultura_nome == 'cultura2':
        atualizar_formato_cultura2(culturas, cultura_nome)