#multiconn-server.py

from pickle import TRUE
import sys
import socket
import selectors
import types

sel = selectors.DefaultSelector()

#HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
#PORT = 65432  # Port to listen on (non-privileged ports are > 1023)

HOST, PORT = sys.argv[1], int(sys.argv[2])
lsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
lsock.bind((HOST, PORT))
lsock.listen()
print(f"Listening on {(HOST, PORT)}")
lsock.setblocking(False)
sel.register(lsock, selectors.EVENT_READ, data=None)


def accept_wrapper(sock):
    conn, addr = sock.accept()  # Should be ready to read
    print(f"Accepted connection from {addr}")
    conn.setblocking(0)
    data = types.SimpleNamespace(addr=addr, inb=b"", outb=b"")
    events = selectors.EVENT_READ | selectors.EVENT_WRITE
    sel.register(conn, events, data=data)

def service_connection(key, mask):
    sock = key.fileobj
    _data = key.data
    if mask & selectors.EVENT_READ:
        recv_data = sock.recv(1024).decode('utf-8')  # Should be ready to read
        if recv_data:
            print(f"Received {recv_data}")
            sock.sendall(bytes(recv_data, 'utf-8'))
        else:
            sel.unregister()
            sel.close()
            print(f"Closing connection to {_data.addr}")
            sock.send(b'Error')

try:
    while True:
        events = sel.select(timeout=None)
        for key, mask in events:
            if key.data is None:
                accept_wrapper(key.fileobj)
            else:
                service_connection(key, mask)
except KeyboardInterrupt:
    print("Caught keyboard interrupt, exiting")
finally:
    sel.close()