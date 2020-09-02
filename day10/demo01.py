import socket

socked = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socked.bind(("127.0.0.1", 8000))
socked.listen(10)
print("waiting for connect....")
connect, addr = socked.accept()
data = connect.recv(1024)
connect.send(b"ok")
print(data.decode())
connect.close()
socked.close()
