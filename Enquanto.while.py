#fazer um programa que lê números inteiros até que um zero seja lido. Ao final msotra a soma dos números lidos.


x:int; soma:int


soma = 0
x = int(input('Digite o primeiro numero: '))

while x != 0:
    soma = soma + x
    x = int(input('Digite outro numero: '))

    print('SOMA = ', soma)