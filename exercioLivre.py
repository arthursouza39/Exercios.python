#Faça um Programa que peça as 4 notas bimestrais e mostre a média.


nota1:int; nota2:int; nota3:int; nota4:int


nota1 =int(input('Digite sua nota1: '))
nota2 =int(input('Digite sua nota2: '))
nota3 =int(input('Digite sua nota3: '))
nota4 =int(input('Digite sua nota4: '))

if nota1 > 12:
    print('SS')
elif nota1 <= 6:
    print('MM')
else:
    print('SR')

if nota2 > 12:
    print('SS')
elif nota2 <= 6:
    print('MM')
else:
    print('SR')

if nota3 > 12:
    print('SS')
elif nota3 <= 6:
    print('MM')
else:
    print('SR')

if nota4 > 12:
    print('SS')
elif nota4 <= 6:
    print('MM')
else:
    print('SR')