import socket
import time

HOST = "127.0.0.1"  # The server's hostname or IP address
PORT = 65400  # The port used by the server

ls=['GET 1','DEL 1','PUT 1 one','PUT 2 two','PUT 3 three','GET 1','GET 2','GET 3','DEL 1','GET 1','PUT 1 one']
#ls=['GET 1','PUT 1 one','GET 1','DEL 1','GET 1']

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    for m in ls:
        time.sleep(2)
        s.sendall(m.encode('utf-8'))
        data=s.recv(1024)
        print(data.decode())
