salarios = [20000, 3000, 3200, 1700, 12000, 3500,]

total = 0

# ! somaremos todos os salarios

for sal in salarios:
    total = total + sal
    print("atual:", total)
    print("total,"," + ", sal, "=")
    total = total + sal
    print(total)
    print("#"*10)

print("-"*50)
print("o total somado e: ", total)