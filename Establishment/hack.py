import socket
import sys

# Check if the correct number of command line arguments are provided
if len(sys.argv) != 4:
    print("Usage: python hack.py <IP address> <port> <message>")
    sys.exit(1)

# Extract command line arguments
ip_address = sys.argv[1]
port = int(sys.argv[2])
message = sys.argv[3]

# Create a new socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    # Connect to the host and port using the socket
    client_socket.connect((ip_address, port))

    # Send the message to the host using the socket
    client_socket.sendall(message.encode())

    # Receive the server's response
    response = client_socket.recv(1024).decode()

    # Print the server's response
    print(response)

finally:
    # Close the socket
    client_socket.close()
