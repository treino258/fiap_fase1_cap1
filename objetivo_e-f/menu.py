from objetivo_a.culturas import cultura_1, cultura_2, culturas

def input_float(mensagem: str) -> float:
    while True:
        try:
            return float(input(mensagem))
        except ValueError:
            print("Valor inválido. Tente novamente.")


# Função para exibir o menu
def exibir_menu():
    print("\nMenu de Opções:")
    print("1 - Entrada de Area")
    print("2 - Saída de Area")
    print("3 - Atualizar Area")
    print("4 - Deletar Area")

    #todo - implementar as opções de entrada, saída, atualização e deleção de ruas

    print("5 - Entrada de Ruas")
    print("6 - Entrada de Ruas")
    print("7 - Saída de Ruas")
    print("8 - Atualizar Ruas")
    print("9 - Deletar Ruas")


    print("0 - Sair do Programa")


# Dicionário para armazenar os dados do manejo (insumo) por cultura
# Exemplo: cultura1 usa 500 mL/m², cultura2 usa 300 mL/m²
insumo_por_metro = {
    "cultura1": 500,  # Em mL/m²
    "cultura2": 300  # Em mL/m²
}


# Função para calcular o manejo de insumo com base na área
def calcular_manejo(cultura, area):
    if cultura in insumo_por_metro:
        insumo = insumo_por_metro[cultura] * area  # Cálculo do insumo necessário
        return insumo
    return 0


# Função para entrada de dados de cultura
def entrada_dados(culturas):
    print("\nEntrada de Dados:")
    cultura_nome = input(f"""
 0 - VOLTAR AO MENU
 1 - {cultura_1}
 2 - {cultura_2}
    """).strip().lower()

    if cultura_nome in ('0', 'voltar ao menu', 'voltar'):
        print("Retornando ao menu principal.")
        return
    if cultura_nome not in {'1', 'cultura1', '2', 'cultura2'}:
        print("Cultura não reconhecida. Retornando ao menu.")
        return
    if cultura_nome in {'1', 'cultura1'}:
        cultura_nome = 'cultura1'

    def entrada_formato():  # Função para entrada de formato do plantio (dentro de entrada_dados)
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
            altura = float(input('Digite as dimensões do primeiro lado: '))
            base = float(input('Digite as dimensões do segundo lado: '))
            area = base * altura
        elif forma_nome in {'2', 'triangular'}:
            print('Você escolheu o plantio Triangular.')
            altura = float(input('Digite a altura do triângulo: '))
            base = float(input('Digite a base do triângulo: '))
            area = (base * altura) / 2

        print(f'A área do plantio é: {area:.2f}m²')
        return area  # Retorna a área calculada

    if cultura_nome in {'2', 'cultura2'}:
        cultura_nome = 'cultura2'

    def entrada_formato():  # Função para entrada de formato do plantio (dentro de entrada_dados)
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
            altura = float(input('Digite as dimensões do primeiro lado: '))
            base = float(input('Digite as dimensões do segundo lado: '))
            area = base * altura
        elif forma_nome in {'2', 'triangular'}:
            print('Você escolheu o plantio Triangular.')
            altura = float(input('Digite a altura do triângulo: '))
            base = float(input('Digite a base do triângulo: '))
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


# Função para atualizar dados de cultura
def atualizar_dados(culturas):
    print("\nEscolha a cultura para atualizar dados:")
    cultura_nome = input(""" 
 0 - VOLTAR AO MENU
 1 - cultura1
 2 - cultura2
    """).strip().lower()

    if cultura_nome in ('0', 'voltar ao menu', 'voltar'):
        print("Retornando ao menu principal.")
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


def atualizar_formato_cultura1(culturas, cultura_nome):  # Função para cultura1
    print("\nEscolha o registro para atualizar:")
    if not culturas[cultura_nome]:
        print("Nenhum dado registrado.")
    else:
        for i, dado in enumerate(culturas[cultura_nome], 1):
            print(f"  Registro {i}: Área = {dado['area']} m², Insumo = {dado['manejo']} mL")

    # Solicita o índice antes de confirmar
    indice = int(input(
        f"Pressione 0 para voltar ao menu. Digite o índice do registro a ser atualizado (1 a {len(culturas[cultura_nome])}): "))

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
    indice = int(input(
        f"Pressione 0 para voltar ao menu. Digite o índice do registro a ser atualizado (1 a {len(culturas[cultura_nome])}): "))

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


# Função para deletar um dado específico dentro de cada cultura
def deletar_formato_cultura(culturas, cultura_nome):
    print("\nEscolha o registro para deletar:")
    if not culturas[cultura_nome]:
        print("Nenhum dado registrado.")
    else:
        for i, dado in enumerate(culturas[cultura_nome], 1):
            print(f"  Registro {i}: Área = {dado['area']} m², Insumo = {dado['manejo']} mL")

    # Solicita o índice antes de confirmar
    indice = int(input(
        f"Pressione 0 para voltar ao menu. Digite o índice do registro a ser deletado (1 a {len(culturas[cultura_nome])}): "))

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


# Função principal para gerenciar o menu
def main():
    # Criando um dicionário para armazenar os dados das culturas
    while True:
        exibir_menu()
        escolha = input("Escolha uma opção (1-4 ou 'Sair'): ").strip().lower()

        if escolha in {'1', 'entrada', 'Entrada de Dados', 'entrada de dados', 'entrar'}:
            entrada_dados(culturas)
        elif escolha in {'2', 'saída', 'saida de dados', 'Saída de Dados'}:
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