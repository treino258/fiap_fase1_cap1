from main.menu import main # Importando a função principal do menu
from main.menu import exibir_menu # Importando a função de exibição do menu
from entrada.dados.py import entrada_dados # Importando a função de entrada de dados
from saida.dados.py import saida_dados # Importando a função de saída de dados
from atualizar.py import atualizar_dados # Importando a função de atualização de dados
from deletar.py import deletar_dados # Importando a função de deleção de dados
from utils.menu.py import calcular_manejo # Importando a função de calcular manejo
from utils.atualizar.py import atualizar_formato_cultura1 # Importando a função de atualização de dados
from utils.atualizar.py import atualizar_formato_cultura2 # Importando a função de atualização de dados
from utils.deletar.py import deletar_formato_cultura # Importando a função de deleção de dados

# Criando um dicionário para armazenar os dados das culturas
culturas = {'cultura1': [], 'cultura2': []}
