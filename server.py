import socket
import sys
import threading
import struct


port = sys.argv[1]
print("waiting on port", port, "...")

BUFSIZE = 1028

def listeningToKeyboard():
    for line in sys.stdin:
        #implements ctrl d and ctrl c always works because of the interrupt signal. Does q need to exit program?
        if line == '^D' or len(line) == 0:
            exit()
        
def listeningToSocket(server_port):
   server_port = int(server_port)
   s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
   s.bind(('', server_port))
   print("Server is ready to listen")
   while True:
       data, addr = s.recvfrom(BUFSIZE)



main_thread = threading.Thread(name = 'main_thread', target = listeningToKeyboard, daemon = None)
main_thread.start()

T1 = threading.Thread(name = 'thread_one', target = listeningToSocket, args = (port,), daemon = True)
T1.start()


