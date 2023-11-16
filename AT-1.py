compras = []
vendas = []

def registrar_compra():
    nome = input("Digite o nome do produto: ")
    quantidade = float(input("Digite a quantidade: "))  
    valorUnitario = float(input("Digite o valor unitário: "))  
    compras.append([nome, quantidade, valorUnitario])
    
def registrar_venda():
    nome = input("Digite o nome do produto: ")
    quantidade = float(input("Digite a quantidade: "))
    valorUnitario = float(input("Digite o valor unitário: "))
    vendas.append([nome, quantidade, valorUnitario])

def calcular_lucro():
    totalCompras = 0
    for i in compras:
        totalCompras += i[1] * i[2]
        
    totalVendas = 0
    for i in vendas:
        totalVendas += i[1] * i[2]
    
    lucro = totalVendas - totalCompras
    print(f"O lucro total é: R${lucro:.2f}")

while True:
    print("MENU:\n")
    print("1 - Registrar uma compra")
    print("2 - Registrar uma venda")
    print("3 - Verificar saldo total das vendas")
    print("4 - Sair\n")

    opcao = input("Escolha uma opção: \n")

    if opcao == "1":
        registrar_compra()
    elif opcao == "2":
        registrar_venda()
    elif opcao == "3":
        calcular_lucro()
    elif opcao == "4":
        print("Volte sempre!")
        break
    else:
        print("Opção inválida. Escolha uma opção de 1 a 4.")



