import socket
import os


def handle_request(client_socket, request):
    filename = request.split()[1][1:]

    if os.path.isfile(filename):
        with open(filename, 'rb') as file:
            response_data = file.read()
        response = b"HTTP/1.1 200 OK\r\n\r\n" + response_data
    else:
        with open('coba.html', 'rb') as file:
            response_data = file.read()
        response = response_data

    client_socket.sendall(response)

def main():
    host = '127.0.0.1'
    port = 8080

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen()

    print(f"Server listening on {host}:{port}")

    while True:
        client_socket, client_address = server_socket.accept()
        print(f"Connection from {client_address}")

        request = client_socket.recv(1024).decode('utf-8')
        print(f"Received request: {request}")

        handle_request(client_socket, request)

        client_socket.close()

if __name__ == "__main__":
    main()
