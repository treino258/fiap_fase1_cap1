from main_menu.py import main # Importando a função principal do menu
from main_menu.py import exibir_menu # Importando a função de exibição do menu
from entrada_dados.py import entrada_dados # Importando a função de entrada de dados
from saida_dados.py import saida_dados # Importando a função de saída de dados
from atualizar.py import atualizar_dados # Importando a função de atualização de dados
from deletar.py import deletar_dados # Importando a função de deleção de dados
from utils_menu.py import calcular_manejo # Importando a função de calcular manejo
from utils_atualizar.py import atualizar_formato_cultura1 # Importando a função de atualização de dados
from utils_atualizar.py import atualizar_formato_cultura2 # Importando a função de atualização de dados
from utils_deletar.py import deletar_formato_cultura # Importando a função de deleção de dados
import culturas.py # Importando o módulo de culturas

# Criando um dicionário para armazenar os dados das culturas
culturas = {'CULTURA_1': [], 'CULTURA_2': []}
