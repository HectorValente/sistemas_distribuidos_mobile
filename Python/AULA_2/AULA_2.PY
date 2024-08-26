def somar_inteiro_e_float(inteiro, expo):
    count = 1
    _resultado = inteiro
    while count < expo:
        _resultado *= inteiro
        count += 1

    return _resultado

# Exemplo de uso
num_inteiro = int(input("Digite um numero inteiro: "))
num_expo = int(input("Digite um numero expoente: "))

resultado = somar_inteiro_e_float(num_inteiro, num_expo)
print(f"O numero {num_inteiro} elevado a {num_expo} e: {resultado}")
