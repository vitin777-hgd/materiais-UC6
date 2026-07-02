# Cria uma lista vazia
numeros = []

# Lê 5 números inteiros
for i in range(5):
    numero = int(input(f"Digite o {i + 1}º número: "))
    numeros.append(numero)

# Exibe os itens da lista
print("Itens da lista:")
for numero in numeros:
    print(numero)