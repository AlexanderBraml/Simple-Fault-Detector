import socketserver
from env import client_ip

class UDPHandler(socketserver.DatagramRequestHandler):

    def handle(self):
        if self.client_address[0] == client_ip:
            if self.rfile.readline().decode().strip() == "1":
                callback()


def callback():
    global callback_
    callback_()


def listen_forever(callback):
    global callback_

    print("Listening on port 6969")
    listen_addr = ('0.0.0.0', 6969)

    callback_ = callback

    socketserver.UDPServer.allow_reuse_address = True 

    serverUDP = socketserver.UDPServer(listen_addr, UDPHandler)
    serverUDP.serve_forever()
