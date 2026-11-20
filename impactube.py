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