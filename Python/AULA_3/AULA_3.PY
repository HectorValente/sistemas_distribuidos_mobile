#1 - utlizando loop for - encontre os multiplos de 3 no range [0,1000)
for i in range(0,1000,1):
    if(i%3==0):
        print("O número {} é multiplo de 3".format(i))