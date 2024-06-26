idade:int
salario: float 
altura:float
sexo:str
nome: str

idade = 20
salario = 5800.5
altura = 1.63
sexo = 'feminino'
nome = 'Maria Silva'
 
print(f'A funcionaria {nome}, sexo {sexo}, ganha {salario: .2f} e tem {idade} anos')

print('A funcionaria {:s}, sexo {:s}, ganha {:2f} e tem {:d} anos'. format(nome, sexo, salario, idade))