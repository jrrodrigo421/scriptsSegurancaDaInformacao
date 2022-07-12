import os
import time

with open('hosts.txt') as file:
    dump = file.read()
    dump = dump.splitlines()

    # print(dump)
    for ip in dump:
        # print(ip)
        print('VERIFICANDO IP:', ip)
        print('*'*60)
        os.system('ping -n 10 {}'.format(ip))
        print('*'*60)
        time.sleep(5)
