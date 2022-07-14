import random, string

tamanho = int(input('Digite o tamano de senha que voce deseja: \n6'))

chars = string.ascii_letters + string.digits + 'Ç!@#$$%¨&*()-_=,.;?'

rnd = random.SystemRandom()

print(''.join(rnd.choice(chars) for i in range(tamanho)))

