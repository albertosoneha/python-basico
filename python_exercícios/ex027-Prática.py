n = str(input('Digite seu nome completo: ')).strip()
nome = n.split()
# print(nome)
# print(nome[0])
print('Muito prazer em te conhecer!')
print('Seu primeiro nome é {}'.format(nome[0]))
# print('Seu último nome é {}'.format(nome[2]))
print('Seu último nome é {}'.format(nome[len(nome)-1]))

