import socketserver
import time

class MyUDPHandler(socketserver.DatagramRequestHandler):

    def handle(self):
        if self.client_address[0] == "192.168.178.60":

            msgRecvd = self.rfile.readline().decode().strip()
            
            if msgRecvd == "1":
                print("alarm", time.time())

if __name__ == '__main__':
    listen_addr = ('0.0.0.0', 6969)

    socketserver.UDPServer.allow_reuse_address = True 

    serverUDP = socketserver.UDPServer(listen_addr, MyUDPHandler)
    serverUDP.serve_forever()
