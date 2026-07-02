numeros = [1, 3, 5, 3, 7, 9, 3]

numero = int(input("Digite um número: "))

quantidade = 0

for valor in numeros:
    if valor == numero:
        quantidade += 1

print(f"O número {numero} aparece {quantidade} vez(es) na lista.")