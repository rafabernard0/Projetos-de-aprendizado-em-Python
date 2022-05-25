# Estudo de funções de sintase em phyton

f1 = input('O que você deseja analizar?   ').strip()

print('Onde começa o Oliveira na frase? ', f1.find('Oliveira'))

print(f'Quantas letras tem no total?   {len(f1)} ')

print('''Quantas letas 'a' existem na frase?  ''', f1.count('a'))

print('Existe a palavra Rafael na frase?  ', 'Rafael' in f1)

print('Será substituido a por A: ', f1.replace('a', 'A'))

print(f'Tudo ficará maiusculo: {f1.upper()} ')

print('Tudo ficará minusculo', f1.lower())

print('Só com a primera maiuscula: ', f1.capitalize())

print('Todo começo maiusculo: ', f1.title())

print('Fazendo cala palavra uma frase separada:  ', f1.split())

print('Fazer um . entre tudo: ',  '.'.join(f1))

f2 = f1.split()

print('Fazer * no split:  ', '*'.join(f2))

print(f'Primeiro e último nome: {f2[0]} {f2[-1]}')

a = str('fim')

print(a.upper())
