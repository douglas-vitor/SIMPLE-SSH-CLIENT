'''
Simples cliente SSH com linha de terminal
V-1
2019
'''
import paramiko

host = input('HOST_IP : ')
port = input('PORTA : ')
user = input('USUARIO : ')
password = input('SENHA : ')

if port == '':
    port=22

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy)
try:
    client.connect(hostname=host, port=port, username=user, password=password)
    print('>>> Escreva exit , para fechar o cliente ssh. <<<\n\n\n')
    while True:
        CMD = input('CMD >> ')
        entrada, saida, erros = client.exec_command(CMD)
        if CMD == 'exit':
            print("Fechando cliente SSH...")
            client.close()
            exit()
        print('--------------------------------------------------')
        print()
        print(saida.readlines())
        print()
        print('--------------------------------------------------')
except Exception as erro:
    print('Erro : ' + str(erro))
    client.close()
    exit()