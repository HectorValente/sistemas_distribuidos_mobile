#Crie uma estrutura de decisão 
#leia a idade de uma pessoa e categorize de acordo com o range abaixo:
#(0,18] - jovem
#(18,40] - adulto
#(40,60] - maduro
#acima de 60 - senior

nNumero = int(input('Por favor, digite um número inteiro para representar uma idade: '));

if(not isinstance(nNumero, int)):
    print("int")
elif(nNumero > 60):
    print("Sênior")
elif(nNumero > 40):
    print("Maduro")
elif(nNumero > 18):
    print("Adulto")
elif(nNumero >= 0):
    print("Jovem")