import socket, threading

def handle(c):
    try:
        # SOCKS5 Handshake
        c.recv(262); c.sendall(b"\x05\x00")
        c.recv(4)
        # الاتصال بسيرفر تليجرام مباشرة
        remote = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        remote.connect(("91.108.56.117", 443)) 
        def f(a, b):
            try:
                while True: b.sendall(a.recv(4096))
            except: pass
        threading.Thread(target=f, args=(c, remote)).start()
        f(remote, c)
    except: pass

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("0.0.0.0", 8443))
s.listen(50)
print("🚀 Simple SOCKS5 is LIVE")
while True:
    conn, _ = s.accept()
    threading.Thread(target=handle, args=(conn,)).start()
