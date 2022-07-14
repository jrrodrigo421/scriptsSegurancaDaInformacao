import socket
import sys

def main():
    try:
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM, 0)
    except socket.error as e:
        print("A conexão falhou!")
        print("Erro: {}" .format(e))
        sys.exit
        print('#'*60)
        print('Socket Criado com SUCESSO!')
        print('#'*60)

    print('*'*60)
    print('*'*60)
    hostAlvo = input('Digite o HOST ou IP a ser conectado: \n')
    portaAlvo = input('Digite e PORTA a ser conectada: \n')
    print('*'*60)
    print('*'*60)   

    try:
        s.connect((hostAlvo, int(portaAlvo)))
        print('Cliente TCP conectado com sucesso')
        s.shutdown(2)
    except socket.error as e:
        print('A conexão falhou')
        print('Erro: {}' .format(e))
        sys.exit()


if __name__ == "__main__":
    main()



