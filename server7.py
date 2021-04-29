# question 7 
# server - bank
import socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('127.0.0.1', 8010))
server.listen(4)
accounts = open("accounts.txt", "r")
text = accounts.readlines()
print(text)

while True:
    connect, address = server.accept()
    received = ''
    while True:
        received = connect.recv(4096)
        if not received:
            break
        received = received.decode('utf-8')
        count = 0
        exists = False
        account = ''
        print(received)
        for line in text:
            if received in line:
                exists = True
                connect.send("Correct Info".encode('utf-8'))
                account = line
                break
            count += 1

        if not exists:
            connect.send("Blocked".encode('utf-8'))
            break
        connect.send("How much money would you like to take out from your account?".encode('utf-8'))
        received = connect.recv(4096)
        if not received:
            break
        received = received.decode('utf-8')
        withdraw_amount = int(received)
        client_info = account.split(':')
        total = int(client_info[2])
        if total >= withdraw_amount:
            total -= withdraw_amount
            client_info[2] = str(total)
            client = ''
            for arg in client_info:
                client += arg + ':'
            client = client[ 0 : len(client)-1]+"\n"
            text[count] = client
            accounts = open("accounts.txt", "w")
            accounts.writelines(text)
            accounts.close()
        connect.send(("total is " + str(total)).encode('utf-8'))
    connect.close()
    print ('the client has disconnected')
