"""04.252.011/0001-10 40.688.134/0001-61 71.506.168/0001-11 12.544.992/0001-05

0   4   2   5   2   0   1   1   0   0   0   1
5   4   3   2   9   8   7   6   5   4   3   2
0   16  6   10  18  0   7   6   0   0   0   2 = 65
Fórmula -> 11 - (65 % 11) = 1
Primeiro digito = 1 (Se o digito for maior que 9, ele se torna 0)

0   4   2   5   2   0   1   1   0   0   0   1   1   X
6   5   4   3   2   9   8   7   6   5   4   3   2
0   20  8   15  4   0   8   7   0   0   0   3   2 = 67
Fórmula -> 11 - (67 % 11) = 10 (Como o resultado é maior que 9, então é 0)
Segundo digito = 0

Novo CNPJ + Digitos = 04.252.011/0001-10
CNPJ Original =       04.252.011/0001-10
Válido

Recap.
543298765432 -> Primeiro digito
6543298765432 -> Segunro digito
"""
from random import randint


def geracnpj():
    num = randint(0, 99999999)
    return str(num) + '0001'


def formata(msg):
    novo_cnpj = ''.join(map(str, msg))
    return novo_cnpj
    # return print(f'{novo_cnpj[:2]}.{novo_cnpj[2:5]}.{novo_cnpj[5:8]}/{novo_cnpj[8:12]}-{novo_cnpj[12:14]}')




'''
Calcula o primeiro dígito que está faltando no cnpj
'''


def firstdigit(cnpj, multiplicador_1):
    soma = 0
    for c in range(0, 12, 1):
        x = cnpj[c] * multiplicador_1[c]
        soma += x

    calc1 = 11 - (soma % 11)
    if calc1 > 9:
        calc1 = 0
        cnpj.append(calc1)
    else:
        cnpj.append(calc1)

    return cnpj


'''
Calcula o segundo dígito que está faltando no cnpj
'''


def seconddigit(cnpj, multiplicador_2):
    soma2 = 0
    for c in range(0, 13, 1):
        x = cnpj[c] * multiplicador_2[c]
        soma2 += x

    calc2 = 11 - (soma2 % 11)
    if calc2 > 9:
        calc2 = 0
        cnpj.append(calc2)
    else:
        cnpj.append(calc2)

    return cnpj


'''
Removendo caracteres do cnpj
'''


def remover_caracter(cnpj):
    cnpj = cnpj.replace('/', '')
    cnpj = cnpj.replace('.', '')
    cnpj = cnpj.replace('-', '')
    return cnpj
