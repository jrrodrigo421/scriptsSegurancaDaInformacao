import hashlib

string = input('Digite o texto a ser gerado a HASH: \n')

menu  = int(input('''##### MENU #####
                    OPCAO 1: MD5
                    OPCAO 2: SHA1
                    OPCAO 3: SHA256
                    OPCAO 4: SHA512
                    OPCAO 5: Finalizar Programa
            Digite a OPCAO  do Hash a ser GERADO: '''))

if menu == 1:
    resultado = hashlib.md5(string.encode('utf-8'))
    print('O Hash MD5 é: \n', string,'é', resultado.hexdigest())
elif menu == 2:
    resultado = hashlib.sha1(string.encode('utf-8'))
    print('O Hash MD5 é: \n', string,'é', resultado.hexdigest())
elif menu == 3:
    resultado = hashlib.sha256(string.encode('utf-8'))
    print('O Hash MD5 é: \n', string,'é', resultado.hexdigest())
elif menu == 4:
    resultado = hashlib.sha512(string.encode('utf-8'))
    print('O Hash MD5 é: \n', string,'é', resultado.hexdigest())
elif menu == 5:
    print('Programa Encerrado')
    exit  
else:
    print('Digite opção CORRETA')



