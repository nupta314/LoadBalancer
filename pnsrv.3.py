import os
import socket
import json

HOST = "127.0.0.1"
try:
    PORT = 65400 + int(os.path.basename(__file__).split('.')[1])
except:
    print('This file is not meant to be run\nRead about.txt')
    exit()

file='srvn.txt'

fp=open(file,'r')
db=json.load(fp)
fp.close()

def fdb(str: str):
    ls=str.split()
    if ls[0] == 'GET':
        return db.get(ls[1],'!400')
    elif ls[0] == 'PUT':
        db[ls[1]]=ls[2]
        return '!200'
    elif ls[0] == 'DEL':
        db.pop(ls[1],'!200')
        return '!200'
    else: return str

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        while True:
            data = conn.recv(1024)
            if not data:
                break
            fp=open(file,'r')
            db=json.load(fp)
            fp.close()
            print(data.decode())
            conn.sendall(fdb(data.decode()).encode('utf-8'))
            fp=open(file,'w')
            json.dump(db,fp)
            fp.close()

fp=open(file,'w')
json.dump(db,fp)
fp.close()