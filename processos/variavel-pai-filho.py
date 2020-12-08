# No código abaixo é criada uma variável chamada idade, inicialmente com valor 50.

# 1. Altere o código para imprimir a mais, dentro do código do pai e do código do filho, a idade, e execute o código, analisando o retorno. No filho, faça print('Idade no filho', idade), e no pai, faça print('Idade no pai', idade)
# 2. Altere o código do filho para, antes de imprimir a idade, alterar a idade para 20. Execute o código e analise o retorno. A impressão da idade, neste momento, era para ser similar no pai e no filho? Por quê?


import os

print('+Sou processo principal (pai). Meu PID é: ', os.getpid())

escolha = input('\nDigite 1 para criar um novo processo, outra tecla para sair:' )

idade = 50
if escolha == '1':
  pid = os.fork()
  if pid == 0:
    print('\n-Sou filho. Meu PID é:' + str(os.getpid()))
    idade = 20
    print('Idade no filho:', idade)
  elif pid > 0:
    print('+Sou pai. Meu PID é:' + str(os.getpid()) + ' Meu filho é: ' + str(pid))
    print('Idade no pai:', idade)
else:
  exit()