//5. Write a program to create a server that listens to port 55 using stream sockets. Write a simple
//client program to connect to the server. The client should request for a text file and the server
//should return the file before terminating the connection — I

// Server Code
import socket 
 
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
port=5004 
server_socket.bind(('localhost', port)) 
server_socket.listen(5) 
print(f"Server listening on port {port}...") 
 
while True: 
        client_socket, client_address = server_socket.accept() 
        print(f"Connection established with {client_address}") 
 
        filename = client_socket.recv(1024).decode('utf-8') 
        print(f"Client requested file: {filename}") 
 
        try: 
            with open(filename, 'rb') as file: 
                file_data = file.read() 
                client_socket.sendall(file_data) 
        except FileNotFoundError: 
            client_socket.sendall(b"File not found") 
 
        client_socket.close() 
        print(f"Connection with {client_address} closed")

// Client Code
import socket 

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
port=5004 
client_socket.connect(('localhost', port)) 

filename = input("Enter the filename: ") 
client_socket.sendall(filename.encode('utf-8')) 

file_data = client_socket.recv(1024) 

print(file_data.decode('utf-8')) 

client_socket.close() 