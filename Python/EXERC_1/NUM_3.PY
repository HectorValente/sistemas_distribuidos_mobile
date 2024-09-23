#Utilize a estrutura da repetição for para retornar todos os 
#números divisíveis por 7 até 1000 (exclusivo).

for i in range(0,1000,1):
    if(i%7 == 0):
        print("O número {} é divisível por 7".format(i))
print("Finalizado!")