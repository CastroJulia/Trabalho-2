#GRUPO:
#Julia Castro da Silva
#Letícia de Jesus Barros

def antes(pa: tuple, pb: tuple) -> bool:
    """Retorna True se o país pa deve ficar à frente do país pb."""
    nome_a, ouro_a, prata_a, bronze_a = pa
    nome_b, ouro_b, prata_b, bronze_b = pb

    if ouro_a != ouro_b:
        return ouro_a > ouro_b
    if prata_a != prata_b:
        return prata_a > prata_b
    if bronze_a != bronze_b:
        return bronze_a > bronze_b
    return nome_a < nome_b


def troca(lista: list, a: int, b: int) -> None:
    guarda = lista[a]
    lista[a] = lista[b]
    lista[b] = guarda


def acha_pior(lista: list, tam: int) -> int:
    """Devolve a posição do pior país entre os 'tam' primeiros."""
    pior = 0
    pos = 1
    while pos < tam:
        if antes(lista[pior], lista[pos]):
            pior = pos
        pos += 1
    return pior


def selection_sort(lista: list) -> None:
    tam = len(lista)
    while tam > 1:
        pior = acha_pior(lista, tam)
        troca(lista, pior, tam - 1)
        tam -= 1


def main() -> None:
    linha = input().strip()
    if not linha:
        return
    qtd = int(linha)
    paises = []
    for _ in range(qtd):
        partes = input().split()
        bronze = int(partes[-1])
        prata = int(partes[-2])
        ouro = int(partes[-3])
        nome = ""
        for i in range(len(partes) - 3):
            if i > 0:
                nome = nome + " "
            nome = nome + partes[i]
        paises.append((nome, ouro, prata, bronze))

    selection_sort(paises)

    for nome, ouro, prata, bronze in paises:
        print(f"{nome} {ouro} {prata} {bronze}")


if __name__ == "__main__":
    main()
