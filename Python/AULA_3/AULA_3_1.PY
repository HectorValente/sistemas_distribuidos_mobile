#2 - utilizando loop while - crie a estrutura de algoritmo do fatorial. Informando o numero a ser buscando.
numero = int(input("Digite um numero inteiro para descobrir o fatorial: "))
fatorial = 1

if numero<0:
    print("Número informado:{} é invalido".format(numero))
elif numero == 0:
    fatorial = 1
    print("fatorial de {} é {}".format(numero, fatorial))
else:
    count = numero
    while (count > 0):
        fatorial*=count
        count-=1
        
    print("fatorial de {} é {}".format(numero, fatorial))



    