#Crie um menu de forma a demonstrar que selecionou as opções abaixo:
#1- inserir
#2- editar
#3- excluir
#4 - ler
#5 - sair
#demais opções retorne para o menu

def switch_case(nMenu):
    if nMenu == 1:
        return "Inserir"
    elif nMenu == 2:
        return "Editar"
    elif nMenu == 3:
        return "Excluir"
    elif nMenu == 4:
        return "Ler"
    elif nMenu == 5:
        return "Sair"
    else:
        return "Opção inválida"

nMenu = 0  # Iniciar com valor fora do intervalo para entrar no loop

while (not(nMenu >= 1 and nMenu <=5)):  # Continua até que o usuário escolha "Sair"
    print("--- Menu ---")
    print("1 - Inserir")
    print("2 - Editar")
    print("3 - Excluir")
    print("4 - Ler")
    print("5 - Sair")

    nMenu = int(input("Digite um número do MENU para acessar: "))

    if (not isinstance(nMenu, int)):
        print("Opção inválida")
    else:
        print(switch_case(nMenu))

print("Programa encerrado.")