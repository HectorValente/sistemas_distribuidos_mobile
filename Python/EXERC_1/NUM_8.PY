#Crie uma lista e armazene de forma dinâmica os dados abaixo:
#- seu nome
#- sua idade
#- seu endereço
#- seu cpf
#Imprima o conteúdo da lista
#Insira o rg na posição 1
#Remova o penultimo dado da lista

# Criando a lista dinamicamente com os dados fornecidos pelo usuário
dados = []

# Solicitando informações do usuário
nome = input("Digite seu nome: ")
idade = input("Digite sua idade: ")
endereco = input("Digite seu endereço: ")
cpf = input("Digite seu CPF: ")

# Armazenando os dados na lista
dados.append(nome)        # Índice 0
dados.append(idade)       # Índice 1
dados.append(endereco)    # Índice 2
dados.append(cpf)         # Índice 3

# Imprimindo o conteúdo da lista
print("\nConteúdo inicial da lista:")
print(dados)

# Inserindo o RG na posição 1
rg = input("Digite seu RG: ")
dados.insert(1, rg)

# Imprimindo a lista após inserção do RG
print("\nConteúdo da lista após inserir RG na posição 1:")
print(dados)

# Removendo o penúltimo dado da lista
dados.pop(-2)

# Imprimindo a lista após a remoção do penúltimo dado
print("\nConteúdo da lista após remover o penúltimo dado:")
print(dados)