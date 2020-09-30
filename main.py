import time, os, random

contador = 0

print('\n')
print('-'*30)
print('\nImprimindo sua tabuada...\n')

tabuadas = []

while contador <= 10:
  op = []
  for i in range(10):
    op.append((i+1) * contador)
  
  tabuadas.append(op)
  print('Tabuada do ' + str(contador) + ' incluída com sucesso!')
  time.sleep(random.random())
  contador = contador + 1

def clear_screen():
  os.system('cls' if os.name == 'nt' else 'clear')


clear_screen()
n = int(input('Tabuada de qual número deseja consultar?\n'))

time.sleep(0.2)
clear_screen()
print(f'Imprimindo tabuada do número {n}\n')

for idx, el in enumerate(tabuadas[n]):
  print(f'{n} x {idx+1} = {el}')