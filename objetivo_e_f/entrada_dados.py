from utils_dados import CULTURA_1
from utils_dados import CULTURA_2
from utils_menu.py import calcular_manejo

# Função para entrada de dados de cultura
def entrada_dados(culturas):
    print("\nEntrada de Dados:")
    cultura_nome = input("""
 0 - VOLTAR AO MENU
 1 - [CULTURA_1]
 2 - [CULTURA_2]
    """).strip().lower()
    
    if cultura_nome in ('0', 'voltar ao menu', 'voltar'):
        print ("Retornando ao menu principal.")
        return
    if cultura_nome not in {'1', 'CULTURA_1', '2', 'CULTURA_2'}:
        print("Cultura não reconhecida. Retornando ao menu.")
        return
    if cultura_nome in {'1', 'CULTURA_1'}:
        cultura_nome = 'CULTURA_1'
    def entrada_formato():# Função para entrada de formato do plantio (dentro de entrada_dados)
        print("\nEscolha a forma do seu terreno:")
        forma_nome = input("""
    0 - VOLTAR 
    1 - Retangular
    2 - Triangular
        """).strip().lower()
        
        if forma_nome == '0' or forma_nome == 'voltar':
            return None  # Retorna None para indicar que o usuário cancelou
        if forma_nome not in {'1', 'retangular', '2', 'triangular'}:
            print("Formato não reconhecido. Retornando à seleção de culturas.")
            return None
        if forma_nome in {'1', 'retangular'}:
            print('Você escolheu o plantio Retangular.')
            altura = input_float('Digite as dimensões do primeiro lado: ')
            base = input_float('Digite as dimensões do segundo lado: ')
            area = base * altura
        elif forma_nome in {'2', 'triangular'}:
            print('Você escolheu o plantio Triangular.')
            altura = input_float('Digite a altura do triângulo: ')
            base = input_float('Digite a base do triângulo: ')
            area = (base * altura) / 2

        print(f'A área do plantio é: {area:.2f}m²')
        return area  # Retorna a área calculada
    if cultura_nome in {'2', 'CULTURA_2'}:
        cultura_nome = 'CULTURA_2'
    def entrada_formato():# Função para entrada de formato do plantio (dentro de entrada_dados)
        print("\nEscolha a forma do seu terreno:")
        forma_nome = input("""
    0 - VOLTAR 
    1 - Retangular
    2 - Triangular
        """).strip().lower()
        
        if forma_nome in ('0', 'voltar'):
            print("Retornando ao menu principal.")
            return None  # Retorna None para indicar que o usuário cancelou
        if forma_nome not in {'1', 'retangular', '2', 'triangular'}:
            print("Formato não reconhecido. Retornando à seleção de culturas.")
            return None
        if forma_nome in {'1', 'retangular'}:
            print('Você escolheu o plantio Retangular.')
            altura = input_float('Digite as dimensões do primeiro lado: ')
            base = input_float('Digite as dimensões do segundo lado: ')
            area = base * altura
        elif forma_nome in {'2', 'triangular'}:
            print('Você escolheu o plantio Triangular.')
            altura = input_float('Digite a altura do triângulo: ')
            base = input_float('Digite a base do triângulo: ')
            area = (base * altura) / 2

        print(f'A área do plantio é: {area:.2f}m²')
        return area  # Retorna a área calculada

    # Capturar a área do terreno
    area = entrada_formato()
    if area is None:  # Se o usuário cancelou, volta ao menu
        return

    # Calcular o manejo de insumo automaticamente com base na cultura e na área
    manejo = calcular_manejo(cultura_nome, area)
    
    culturas[cultura_nome].append({'area': area, 'manejo': manejo})
    print(f"Dados de {cultura_nome} registrados com sucesso. Manejo de insumo calculado: {manejo} mL.")
