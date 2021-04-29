# question 7
# client
import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 8010))
c_name = input("enter name: ")
c_code = input("enter code: ")
account = (c_name + ":" + c_code)
client.send(account.encode('utf-8'))
received = client.recv(4096).decode('utf-8')
print(received)

if received == "Blocked":
    client.close()
else:
    received = client.recv(4096).decode('utf-8')
    print(received)
    withdraw_amount = input()
    client.send(withdraw_amount.encode('utf-8'))
    received = client.recv(4096).decode('utf-8')
    print(received)
    client.close()