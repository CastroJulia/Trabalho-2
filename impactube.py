#GRUPO:
#Julia Castro da Silva
#Letícia de Jesus Barros

def coleta_canais() -> list[list]:
    canais = []
    qtd = int(input())
    for i in range(qtd):
        linha = input()
        nome, inscritos, monetizacao, meta = linha.split(';')
        nome = str(nome)
        inscritos = int(inscritos)
        monetizacao = float(monetizacao)
        meta = (meta == 'sim')
        registro = [nome, inscritos, monetizacao, meta]
        canais.append(registro)
    x = float(input())
    y = float(input())
    for registro in canais:
        registro.append(x)
        registro.append(y)
    return canais

def maximo_colunas(tabela: list[list], campo: int) -> int:
    max_colunas = 0
    for registro in tabela:
        colunas_campo = len(registro[campo])
        if colunas_campo > max_colunas:
            max_colunas = colunas_campo
    return max_colunas

def troca(L: list, i: int, j: int) -> None:
    temp = L[i]
    L[i] = L[j]
    L[j] = temp


def codigo_minusculo(c: str) -> int:
    cod = ord(c)
    if 65 <= cod <= 90:                    # 'A' a 'Z'
        cod += 32
    elif 192 <= cod <= 222 and cod != 215: # 'À' a 'Þ' (exceto '×')
        cod += 32
    return cod


def vem_depois(a: str, b: str) -> bool:
    """Retorna True se o nome a deve ficar depois do nome b"""
    i = 0
    while i < len(a) and i < len(b):
        ca = codigo_minusculo(a[i])
        cb = codigo_minusculo(b[i])
        if ca != cb:
            return ca > cb
        i += 1
    return len(a) > len(b)


def empurra(L: list, n: int) -> None:
    i = 0
    while i < n - 1:
        if vem_depois(L[i][0], L[i + 1][0]):
            troca(L, i, i + 1)
        i += 1


def bubbleSort(L: list) -> None:
    n = len(L)
    while n > 1:
        empurra(L, n)
        n -= 1

def calcula_bonus(canais: list[list]) -> list[list]:
    tbBonus = []
    for canal in canais:
        nome, inscritos, monetizacao, meta, x, y = canal
        if meta:
            taxa = x
        else:
            taxa = y
        valor = monetizacao + (inscritos // 1000) * taxa
        tbBonus.append([nome, valor])
    bubbleSort(tbBonus)
    return tbBonus

def exibe_bonus(tbBonus):
    borda = 5
    print('-' * borda)
    print('BÔNUS')
    print('-' * borda)
    for nome, valor in tbBonus:
        print(f'{nome}: R$ {valor:.2f}')

def main():
    canais = coleta_canais()
    bonus = calcula_bonus(canais)
    exibe_bonus(bonus)

if __name__ == '__main__':
    main()