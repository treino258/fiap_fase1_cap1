culturas = []


def calcular_area(tipo: str, base: float, altura: float):
    if tipo == "Cana-de-açúcar":
        return base * altura
    elif tipo == "Milho":
        return base * altura 
    else:
        return 'Digite um valor válido*'


def calcular_insumos(tipo, area: float, consumo_por_metro: float):
    return area * consumo_por_metro  

def adicionar_cultura():
    print("\nCadastro de nova cultura:")
    tipo = input("Digite o tipo de cultura (Cana-de-açúcar ou Milho): ")
    
    if tipo not in ["Cana-de-açúcar", "Milho"]:
        print("🚨 Cultura inválida! Tente novamente.")
        return
    
    base = float(input("Digite a largura do terreno (em metros): "))
    altura = float(input("Digite o comprimento do terreno (em metros): "))
    area = calcular_area(tipo, base, altura)

    consumo_por_metro = float(input("Digite o consumo de insumo por metro quadrado: "))
    insumos_necessarios = calcular_insumos(tipo, area, consumo_por_metro)

    culturas.append({
        "Tipo": tipo,
        "Área": area,
        "Consumo de insumos": insumos_necessarios
    })
    print("\n✅ Cultura adicionada com sucesso!\n")

def exibir_culturas():
    if not culturas:
        print("\n🚨 Nenhuma cultura cadastrada ainda!\n")
        return

    print("\n📋 Culturas cadastradas:")
    for i, cultura in enumerate(culturas):
        print(f"{i + 1}. Tipo: {cultura['Tipo']} - Área: {cultura['Área']} m² - Insumos: {cultura['Consumo de insumos']} L")


def menu():
    while True:
        print("\n🌱 **Sistema de Gerenciamento Agrícola** 🌱")
        print("1️⃣ - Adicionar Cultura")
        print("2️⃣ - Exibir Culturas")
        print("3️⃣ - Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            adicionar_cultura()
        elif opcao == "2":
            exibir_culturas()
        elif opcao == "3":
            print("\n👋 Saindo do sistema... Até mais!\n")
            break
        else:
            print("\n🚨 Opção inválida! Tente novamente.\n")

if __name__ == "__main__":
    menu()
