#GRUPO:
#Julia Castro da Silva
#Letícia de Jesus Barros

salario, qtdMeses, valorDesejado = map(float, input().split())
valorMinimo, tmpMeses, porcRend = map(float, input().split())

valorFinal = salario * (1 + (porcRend / 100))

condicao1 = salario >= valorMinimo
condicao2 = tmpMeses <= qtdMeses
condicao3 = valorFinal >= valorDesejado 

if condicao1 and condicao2 and condicao3:
    print("invista!")
else:
    print("nao invista!")
