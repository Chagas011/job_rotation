
valor = int(input('informe um numero para a sequencia de Fibonacci: '))


def sequencia_fibonacci(valor):
    anterior = 0
    proxima = 1
    soma = 1
    lista = []
    for _ in range(0, valor + 1):
        lista.append(anterior)
        soma = anterior + proxima
        anterior = proxima
        proxima = soma

    if valor in lista:
        print(f'O numero informado: [{valor}] esta na lista {lista}')

    else:
        print(f'O numero informado: [{valor}] nao esta na lista {lista}')
