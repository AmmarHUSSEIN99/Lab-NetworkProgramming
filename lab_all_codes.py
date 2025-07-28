
# ----------------------------
# UDP CLIENT
# ----------------------------
import socket

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client.sendto(b"Hello server", ("localhost", 5005))
data, addr = client.recvfrom(1024)
print(data.decode())
client.close()

# ----------------------------
# UDP SERVER
# ----------------------------
import socket

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind(("localhost", 5005))
data, addr = server.recvfrom(1024)
server.sendto(data, addr)

# ----------------------------
# TCP CLIENT
# ----------------------------
import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("localhost", 5005))
client.send(b"Hello server")
data = client.recv(1024)
print(data.decode())
client.close()

# ----------------------------
# TCP SERVER
# ----------------------------
import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("localhost", 5005))
server.listen(1)
conn, addr = server.accept()
data = conn.recv(1024)
conn.send(data)
conn.close()

# ----------------------------
# RTT CLIENT
# ----------------------------
import socket
import time

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("localhost", 5005))
start = time.time()
client.send(b"Hello")
data = client.recv(1024)
end = time.time()
print((end - start) * 1000, "ms")
client.close()

# ----------------------------
# RTT SERVER
# ----------------------------
import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("localhost", 5005))
server.listen(1)
conn, addr = server.accept()
data = conn.recv(1024)
conn.send(data)
conn.close()


