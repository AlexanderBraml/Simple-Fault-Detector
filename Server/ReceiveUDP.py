import socketserver
import time

class UDPHandler(socketserver.DatagramRequestHandler):

    def handle(self):
        if self.client_address[0] == "192.168.178.60":

            msgRecvd = self.rfile.readline().decode().strip()
            
            if msgRecvd == "1":
                callback()
                print("alarm", time.time())


def callback():
    global callback_
    callback_()


def listen_forever(callback):
    global callback_
    listen_addr = ('0.0.0.0', 6969)

    callback_ = callback

    socketserver.UDPServer.allow_reuse_address = True 

    serverUDP = socketserver.UDPServer(listen_addr, UDPHandler)
    serverUDP.serve_forever()
