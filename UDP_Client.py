
import socket

target_host = '127.0.0.1'
target_port = 9997

#create socket object

#socket.sock_DGRAM = Datagram for UDP connection
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


#send some data

#Don't need to ensure connection in advance because UDP is stateless
client.sendto(b"AAABBBCCC", (target_host,target_port))


#receive some data
data, addr = client.recvfrom(4096)

print(f"Recived: {data.decode()} from {addr[0]:addr{1}}")
client.close()