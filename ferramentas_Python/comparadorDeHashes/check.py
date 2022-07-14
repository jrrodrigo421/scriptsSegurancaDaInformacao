import hashlib

arquivo1 = 'a.txt'
arquivo2 = 'b.txt'

hash1 = hashlib.new('ripemd160')
hash1.update(open(arquivo1, 'rb').read())

hash2 = hashlib.new('ripemd160')
hash2.update(open(arquivo2, 'rb').read())

if hash1.digest() != hash2.digest():
    print(f'O arqiovo: {arquivo1} é diferente do arquivo: {arquivo2}')
else:
    print(f'O aqruivo: {arquivo1} é igual ao arquivo: {arquivo2}')



