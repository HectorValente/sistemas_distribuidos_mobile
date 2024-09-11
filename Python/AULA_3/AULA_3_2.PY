print("1. cadastrar")
print("2. editar")
print("3. alterar")

opcao = int(input("insira a sua opção:"))

match opcao:
    case 1: print("entrou na opção cadastrar") 
    case 2: print("entrou na opção editar") 
    case 3: print("entrou na opção alterar") 
    case _: print("entrou na opção invalida") 