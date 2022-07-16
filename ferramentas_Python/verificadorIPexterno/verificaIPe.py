import re
import json
from urllib.request import urlopen

url = 'https://ipinfo.io/json'

resposta = urlopen(url)

dados = json.load(resposta)

ip = dados['ip']
org = dados['org']
cid = dados['city']
pais = dados['country']
regiao = dados['region']
print('#'*60)
print('Detalhes do seu IP:  \n')
print('IP: {4}\nRegião {1}\nPaís{2}\nCidade {3}\nOrg: {0}\n'.format(org, regiao, pais, cid, ip))
print('#'*60)
