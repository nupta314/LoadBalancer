import socket

HOST="127.0.0.1"
PORT=65400

n=4 #numbers of servers
p=[]
l=0
for i in range(n):
    s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST,PORT+1+i))
    p.append(s)

client=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.bind((HOST,PORT))
client.listen()
conn,addr=client.accept()
with conn:
    while True:
        data = conn.recv(1024)
        if not data: break
        print(data.decode())
        p[l%n].sendall(data)
        conn.sendall(p[l%n].recv(1024))
        l+=1

client.close()
for i in p:
    i.close()