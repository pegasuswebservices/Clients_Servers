#Create a standard multi threaded TCP server

import socket
import threading

IP = '0.0.0.0'  #localhost
PORT = 9998

def main():

    #Defines server as standard IPv4 Hostname, and TCP Server
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server.bind((IP, PORT)) #Binds the server to the IP and Port of Device
    server.listen(5)    #Server starts listenin with max Backlog cononections
                        #Set to 5.


    print(f'[*] Listening on {IP}:{PORT}')

    while True:  #Server in it's main loop while it waits for connection attempt.
        client, address = server.accept()   #We recevive CLIENT SOCKET in client variable.    # We receive client IP and PORT in Address Tuple
        print(f'[*] Accepted connection from {address[0]}:{address[1]}') #address[0] is client IP   address[1] is client PORT

        #We create new Thread object that points to the handle_client function.
        #This is so the server can accept incoming connections and handle already connected clients at the same time. Hence Threading
        client_handler = threading.Thread(target=handle_client, args=(client,))  #client,   tuple holds the   CLIENT SOCKET  information.  
        client_handler.start()



def handle_client(client_socket):  #client,   tuple  gets passed into client_socket   paramter so  handle client funciton has access to CLIENT SOCKET
    with client_socket as sock:
        request = sock.recv(4096)    #Recives information from CLIENT
        print(f'[*] Received: {request.decode()}')
        sock.send(b"ACK")



if __name__=='__main__':
    main()