#Baseado na teoria de conjunto abordado:
#Crie um conjunto para armazenar os e-mails informados até chegar o tamanho 10.

sMeuconjunto = set()

while (len(sMeuconjunto) < 10):
    email = input("\nDigite um e-mail:\n")
    sMeuconjunto.add(email)

print("\nE-mails armazenados:")
print(sMeuconjunto)