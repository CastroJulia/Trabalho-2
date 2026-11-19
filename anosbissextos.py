#GRUPO:
#Julia Castro da Silva
#Letícia de Jesus Barros

inicio = int(input())
fim = int(input())

contador = 0

for ano in range(inicio, fim + 1):
    if (ano % 4 == 0 and ano % 100 != 0) or ano % 400 == 0:
        print(ano)
        contador += 1

print("bissextos:", contador)
