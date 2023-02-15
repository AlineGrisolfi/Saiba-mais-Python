''' Um professor quer sortear 1 de seus 4 alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome
deles e escrevendo o nome do escolhido. '''

import random
n1 = input('Informe o nome do 1 aluno: ')
n2 = input('Informe o nome do 2 aluno: ')
n3 = input('Informe o nome do 3 aluno: ')
n4 = input('Informe o nome do 4 aluno: ')
lista = [n1, n2, n3, n4]
escolhido = random.choice(lista)
print('O escolhido foi {}'.format(escolhido))

''' Para este programa foi usado o módulo random.
Este módulo implementa geradores de números pseudoaleatórios para várias distribuições.'''