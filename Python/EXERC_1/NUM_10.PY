#Crie uma tupla com itens do lanche padrão numero 1 do MC Donalds (Big Mac).
#Nesta tupla o cliente deseja alterar o item batata-frita media por uma batata frita grande.
#Reproduza isto no codigo da tupla.

# Tupla original com os itens do lanche padrão número 1 do McDonald's
lanche_padrao = ("Big Mac", "Batata Frita Média", "Refrigerante Médio")

# Exibindo a tupla original
print("Lanche padrão:", lanche_padrao)

# Alterando o item 'Batata Frita Média' para 'Batata Frita Grande'
# Como tuplas são imutáveis, criamos uma nova tupla com a alteração
lanche_personalizado = (lanche_padrao[0], "Batata Frita Grande", lanche_padrao[2])

# Exibindo a nova tupla com a alteração
print("Lanche personalizado:", lanche_personalizado)