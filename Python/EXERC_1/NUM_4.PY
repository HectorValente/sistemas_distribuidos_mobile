#Com estrutura de repetição while
#Comece um contador em 10000 e retorne os números naturais divisiveis 
# por 2 e 3 de forma regressiva.

iCount = 10000
while (iCount >= 0):
    if (iCount%2 == 0):
        if (iCount%3 == 0):
            print("O número {} é divisivel por 2 e 3".format(iCount))
    iCount -= 1
print("Todos os números divisiveis por 2 e 3 já foram demonstrados.")