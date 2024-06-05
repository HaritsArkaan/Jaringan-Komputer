import socket
import sys
import webbrowser
import os

def main():
    if len(sys.argv) != 4:
        print("Usage: client.py server_host server_port filename")
        return

    server_host = sys.argv[1]
    server_port = int(sys.argv[2])
    filename = sys.argv[3]

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        client_socket.connect((server_host, server_port))

        request = f"GET /{filename} HTTP/1.1\r\nHost: {server_host}:{server_port}\r\n\r\n"
        client_socket.sendall(request.encode('utf-8'))

        response = client_socket.recv(4096)
        
        if response.startswith(b"HTTP/1.1 200 OK"):
            print("HTTP/1.1 200 OK")
            print("Opening the HTML content in a web browser...")
            with open("temp.html", "wb") as temp_file:
                temp_file.write(response)
            url = f"file://{os.path.abspath('temp.html')}"
            webbrowser.open(url)
        else:
            print("HTTP/1.1 404 Not Found")
            with open("temp.html", "wb") as temp_file:
                temp_file.write(response)
            url = f"file://{os.path.abspath('temp.html')}"
            webbrowser.open(url)
    except Exception as e:
        print(f"Error: {e}")
    finally:
        client_socket.close()

if __name__ == "__main__":
    main()
