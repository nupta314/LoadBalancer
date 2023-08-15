import socket
import pickle

HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT = 65400  # Port to listen on (non-privileged ports are > 1023)
P1 = 65401
P2 = 65402

with open('srv1.pkl','rb') as fp:
    db=pickle.load(fp)
    s1k=set(db.keys())
with open('srv2.pkl','rb') as fp:
    db=pickle.load(fp)
    s2k=set(db.keys())
db=False

s1sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s1sock.connect((HOST,P1))

s2sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s2sock.connect((HOST,P2))

def fdb(str : str):
    ls=str.split()
    if ls[1] in s1k:
        if ls[0] == 'DEL':
            s1k.remove(ls[1])
        s1sock.sendall(str.encode('utf-8'))
        return s1sock.recv(1024)
    elif ls[1] in s2k:
        if ls[0] == 'DEL':
            s2k.remove(ls[1])
        s2sock.sendall(str.encode('utf-8'))
        return s2sock.recv(1024)
    #following branches can be optimized
    elif len(s1k) <= len(s2k):
        if ls[0] == 'PUT':
            s1k.add(ls[1])
        s1sock.sendall(str.encode('utf-8'))
        return s1sock.recv(1024)
    else:
        if ls[0] == 'PUT':
            s2k.add(ls[1])
        s2sock.sendall(str.encode('utf-8'))
        return s2sock.recv(1024)

clsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clsock.bind((HOST,PORT))
clsock.listen()
conn,addr = clsock.accept()
with conn:
    while True:
        data = conn.recv(1024)
        if not data:
            break
        conn.sendall(fdb(data.decode()))

s1sock.close()
s2sock.close()
clsock.close()
