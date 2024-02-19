//4. Write a program to create a chat server that listens to port 54 using stream sockets. Write a
//simple client program to connect to the server. Send multiple text messages from the client to
//the server and vice versa. When either party types "Bye", close the connection - 1 

// Server Code
import socket 
 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
port = 5004 
s.bind((socket.gethostname(), port)) 
s.listen(10) 
 
print("Waiting for a connection...") 
c, adr = s.accept() 
print(f"Connected to {adr} established") 
 
while True: 
    message_to_send = input("Server: ") 
    c.send(bytes(message_to_send, "utf-8")) 
 
    if message_to_send.lower() == "bye": 
        print(f"Connection with {adr} closed.") 
        break 
 
    data = c.recv(1024) 
    if not data: 
        break 
    print(f"Client: {data.decode()}") 
 
print(f"Connection with {adr} closed.") 
c.close() 

// Client Code
import socket 
 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
port = 5004 
s.connect((socket.gethostname(), port)) 
 
while True: 
    data = s.recv(1024) 
    if not data: 
        break 
    print(f"Server: {data.decode()}") 
 
    if data.decode().lower() == "bye": 
        print("Connection closed by the server.") 
        break 
 
    message_to_send = input("Client: ") 
    s.send(bytes(message_to_send, "utf-8")) 
 
    if message_to_send.lower() == "bye": 
        print("Connection closed.") 
        break 
 
s.close()