import socket
import threading

def handle_client(connection):
    try:
        # SOCKS5 Handshake
        data = connection.recv(262)
        connection.sendall(b"\x05\x00")
        
        # الاتصال بالوجهة (تليجرام أو غيره)
        data = connection.recv(4)
        # تشغيل التمرير
        remote = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        remote.connect(("91.108.56.117", 443)) # IP تليجرام العالمي
        
        def forward(src, dst):
            try:
                while True:
                    data = src.recv(4096)
                    if not data: break
                    dst.sendall(data)
            except: pass

        threading.Thread(target=forward, args=(connection, remote)).start()
        forward(remote, connection)
    except:
        pass

if __name__ == "__main__":
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('0.0.0.0', 8443))
    server.listen(100)
    print("🚀 SOCKS5 Server Live on 8443")
    while True:
        conn, addr = server.accept()
        threading.Thread(target=handle_client, args=(conn,)).start()
