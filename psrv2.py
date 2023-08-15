import socket
import pickle

HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT = 65402  # Port to listen on (non-privileged ports are > 1023)

with open('srv2.pkl','rb') as fp:
    db=pickle.load(fp)

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
            print(data.decode())
            conn.sendall(fdb(data.decode()).encode('utf-8'))

with open('srv2.pkl','wb') as fp:
    pickle.dump(db,fp)