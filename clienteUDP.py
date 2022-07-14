import socket
from ssl import SSL_ERROR_INVALID_ERROR_CODE
from typing import final

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
print('Cliente socket criado com Sucesso')

host = 'localhost'
porta = 5433
mensagem = 'Olá Server'

try:
    print('Cliente: ' + mensagem)
    s.sendto(mensagem.encode(), (host, 5432))

    dados, servidor = s.recvfrom(4096)
    dados = dados.decode()
    print('Cliente' + dados)
finally:
    print('Cliente: Fechando a conexão')
    s.close()
    