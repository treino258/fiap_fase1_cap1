from utils.dados.py import cultura1
from utils.dados.py import cultura2

def atualizar_formato_cultura1(culturas, cultura_nome):  # Função para cultura1
    print("\nEscolha o registro para atualizar:")
    if not culturas[cultura_nome]:
        print("Nenhum dado registrado.")
    else:
        for i, dado in enumerate(culturas[cultura_nome], 1):
            print(f"  Registro {i}: Área = {dado['area']} m², Insumo = {dado['manejo']} mL")
    
    # Solicita o índice antes de confirmar
    indice = int(input(f"Pressione 0 para voltar ao menu. Digite o índice do registro a ser atualizado (1 a {len(culturas[cultura_nome])}): "))
    
    if indice == 0:
        print("Retornando ao menu principal.")
        return

    if indice < 1 or indice > len(culturas[cultura_nome]):
        print("Índice inválido,retornando ao menu principal.")
        return
    
    print(f"Você escolheu atualizar o registro {indice}. E isso mesmo? ")
    confirmacao = input("""
    0 - NÃO
    1 - SIM
    """).strip().lower()
    
    # Verificação de confirmação
    if confirmacao in ('0', 'não', 'nao', 'n', 'no', 'NÃO', 'NAO', 'N', 'NO'):
        print("Operação cancelada. Retornando ao menu.")
        return  # Cancela a operação
    elif confirmacao == '1' or confirmacao == 'sim':
        print("\nEscolha a nova forma do seu terreno para a plantacao de (cultura1):")
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

        # Calcula a área para cultura1
        if forma_nome in {'1', 'retangular'}:
            print('Você escolheu o plantio Retangular.')
            altura = float(input('Digite as dimensões do primeiro lado: '))
            base = float(input('Digite as dimensões do segundo lado: '))
            area = base * altura
        elif forma_nome in {'2', 'triangular'}:
            print('Você escolheu o plantio Triangular.')
            altura = float(input('Digite a altura do triângulo: '))
            base = float(input('Digite a base do triângulo: '))
            area = (base * altura) / 2
        
        # Atualiza o dado no registro escolhido
        culturas[cultura_nome][indice - 1]['area'] = area
        culturas[cultura_nome][indice - 1]['manejo'] = area * 500  # Ou o cálculo apropriado

        print(f'A área foi atualizada com sucesso. A nova área do plantio é: {area:.2f}m²')
        return area  # Retorna a área calculada

def atualizar_formato_cultura2(culturas, cultura_nome):  # Função para cultura2
    print("\nEscolha o registro para atualizar:")
    if not culturas[cultura_nome]:
        print("Nenhum dado registrado.")
    else:
        for i, dado in enumerate(culturas[cultura_nome], 1):
            print(f"  Registro {i}: Área = {dado['area']} m², Insumo = {dado['manejo']} mL")
    
    # Solicita o índice antes de confirmar
    indice = int(input(f"Pressione 0 para voltar ao menu. Digite o índice do registro a ser atualizado (1 a {len(culturas[cultura_nome])}): "))
    
    if indice == 0:
        print("Retornando ao menu principal.")
        return

    if indice < 1 or indice > len(culturas[cultura_nome]):
        print("Índice inválido,retornando ao menu principal.")
        return
    
    print(f"Você escolheu atualizar o registro {indice}. E isso mesmo? ")
    confirmacao = input("""
    0 - NÃO
    1 - SIM
    """).strip().lower()
    
    # Verificação de confirmação
    if confirmacao in ('0', 'não', 'nao', 'n', 'no', 'NÃO', 'NAO', 'N', 'NO'):
        print("Operação cancelada. Retornando ao menu.")
        return  # Cancela a operação
    elif confirmacao == '1' or confirmacao == 'sim':
        print("\nEscolha a nova forma do seu terreno para a plantacao de (cultura1):")
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

        # Calcula a área para cultura1
        if forma_nome in {'1', 'retangular'}:
            print('Você escolheu o plantio Retangular.')
            altura = float(input('Digite as dimensões do primeiro lado: '))
            base = float(input('Digite as dimensões do segundo lado: '))
            area = base * altura
        elif forma_nome in {'2', 'triangular'}:
            print('Você escolheu o plantio Triangular.')
            altura = float(input('Digite a altura do triângulo: '))
            base = float(input('Digite a base do triângulo: '))
            area = (base * altura) / 2
        
        # Atualiza o dado no registro escolhido
        culturas[cultura_nome][indice - 1]['area'] = area
        culturas[cultura_nome][indice - 1]['manejo'] = area * 500  # Ou o cálculo apropriado

        print(f'A área foi atualizada com sucesso. A nova área do plantio é: {area:.2f}m²')
        return area  # Retorna a área calculada
