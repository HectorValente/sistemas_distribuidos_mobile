#Leia de forma dinâmica o nome do usuario e sua idade.xx
#Crie a cadeia de caracteres formatando devidamente de forma a trazer a sentença abaixo:
#"Bem-vindo, !  Sua idade é anos.

sNome = str(input("Por favor, escreva o seu nome para acessar o sistema: "))
iIdade = int(input("Por favor, digite a sua idade: "))
print("Você digitou {} e {} anos, correto?".format(sNome, iIdade))