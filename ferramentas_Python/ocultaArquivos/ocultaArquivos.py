import ctypes

atributo_ocultar = 0x02

retorno = ctypes.windll.kernel32.SetFileAttributesW('teste.txt', atributo_ocultar)

if retorno:
    print('\n Arquivo foi Ocultado \n')
else:
    print('\n Arquivo nao foi ocultado \n')
