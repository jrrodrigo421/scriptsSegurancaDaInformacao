#contador de IP uma subrede, somador de IPs, entre outras funcoes

from email.policy import strict
import ipaddress

ip = '192.168.0.0/24'

rede = ipaddress.ip_network(ip, strict=False)
for ip in rede:
    print(ip)

# endereco = ipaddress.ip_address(ip)

# print(endereco + 100)
# print(ip)

# print(rede)
