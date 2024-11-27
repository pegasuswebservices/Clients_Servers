#Many times during pentests, we need to create a TCP client to test for 
#services, fuzz or perform a ton of other tasks.
#Sometimes you won't have the luxury of having networking tools

#Someitmes you'll miss the complete basics - like not being able to conect to the internet

#so we'd need to make a TCP client and server to achevie this



import socket

#Target we want to connect to
target_host = "www.google.com"
target_port = 80


#Create a  socket object
    #AF_INET is standard ipv4 address or hostname
    #SOCK_STREAM is TCP
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


#Connect the client to the target server
client.connect((target_host, target_port))


#Send some data fromt client TO server
client.send(b"GET / HTTP/1.1\r\nHost: google.com\r\n\n")


#Receive some data from the host
response = client.recv(4096)

print(response.decode())

client.close()


#Note this is a quick and dirty tool and it makes serious assumpotions about the sockets.
