from Aula_38_desafio_cnpj.modulos import *

# cnpj_entrada = geracnpj()

try:
    cnpj_entrada = remover_caracter(input('Digite o cnpj: '))
    validar = cnpj_entrada
    cnpj_entrada = cnpj_entrada[:12]

    multiplicador_1 = list(range(5, 1, -1)) + list(range(9, 1, -1))
    multiplicador_2 = list(range(6, 1, -1)) + list(range(9, 1, -1))

    cnpj = [int(x) for x in cnpj_entrada if x.isnumeric()]

    #  Função calcula o primeiro dígito para validação do cnpj
    firstdigit(cnpj, multiplicador_1)

    # Função calcula o segundo dígito para validação do cnpj
    seconddigit(cnpj, multiplicador_2)

    # Função que formata string para imprimir
    novo_cnpj = formata(cnpj)

    if novo_cnpj == validar:
        print(f'O CNPJ: {novo_cnpj[:2]}.{novo_cnpj[2:5]}.{novo_cnpj[5:8]}/{novo_cnpj[8:12]}-{novo_cnpj[12:14]} é válido')
    else:
        print(f'O CNPJ: {validar[:2]}.{validar[2:5]}.{validar[5:8]}/{validar[8:12]}-{validar[12:14]} é inválido')


except (ValueError, TypeError, IndexError):
    print('Digite um valor válido.')


