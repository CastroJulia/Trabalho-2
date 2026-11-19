#GRUPO:
#Julia Castro da Silva
#Letícia de Jesus Barros

def troca(L: list, i: int, j: int) -> None:
    temp = L[i]
    L[i] = L[j]
    L[j] = temp


def empurra(L: list, n: int) -> None:
    """
    Empurra o item max de L para a sua última posição
    e continua até a ordenação estar completa
    """
    i = 0
    while i < n - 1:
        if L[i] > L[i + 1]:
            troca(L, i, i + 1)
        i += 1


def bubbleSort(L: list) -> None:
    n = len(L)  # tamanho da parte não ordenada
    while n > 1:
        empurra(L, n)
        n -= 1


def ordenada(conjunto: set) -> list:
    L = list(conjunto)
    bubbleSort(L)
    return L


noiva = set()
noivo = set()

while True:
    linha = input().strip()
    if linha == "ACABOU":
        break
    nome, quem = linha.rsplit(";", 1)
    nome = nome.strip()
    quem = quem.strip()
    if quem == "noiva":
        noiva.add(nome)
    elif quem == "noivo":
        noivo.add(nome)

listas = [
    ("LISTA FINAL", ordenada(noiva | noivo)),
    ("APENAS NOIVA", ordenada(noiva - noivo)),
    ("APENAS NOIVO", ordenada(noivo - noiva)),
    ("POR AMBOS", ordenada(noiva & noivo)),
    ("POR APENAS UM DELES", ordenada(noiva ^ noivo)),
]

borda = "-" * 20
for i, (titulo, nomes) in enumerate(listas):
    print(borda)
    print(titulo)
    print(borda)
    for nome in nomes:
        print(nome)
    if i < len(listas) - 1:
        print("*")
