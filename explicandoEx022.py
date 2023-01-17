nome = str(input('Digite seu nome: ')).strip()
print('Seu nome em maiusculo é {}:'.format(nome.upper()))
print('Seu nome em minusculo é {}:'.format(nome.lower()))
print('Seu nome tem ao todo {} letras: '.format(len(nome) - nome.count(' ')))
separa = nome.split()
print('Seu primeiro nome é {} e ele tem {} letras:'.format(separa[0], len(separa[0])))


 
'''strip( ) – remove espaços vazios no início e fim do objeto.
upper( ) – troca o que estiver em minusculo para maiúsculo. 
lower( ) - troca o que estiver em maiúsculo para minusculo.
len( ) - verifica o comprimento.
count(‘ ‘) - vai contar quantas vezes o que esta entre as aspas aparece.
split() – divide a frase em palavras.'''