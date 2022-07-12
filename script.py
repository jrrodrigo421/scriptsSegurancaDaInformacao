import os
print('#'*60)
ip_ou_host = input('Digite o IP ou HOST a ser verificado\n\n')
print('-'*60)
os.system('ping -n 10 {}'.format(ip_ou_host))
print('-'*60)

''