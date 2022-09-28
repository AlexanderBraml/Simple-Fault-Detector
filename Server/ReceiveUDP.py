import socketserver
from env import client_ip
from logger import log_udp

class UDPHandler(socketserver.DatagramRequestHandler):

    def handle(self):
        if self.client_address[0] == client_ip:
            msg = self.rfile.readline().decode().strip()
            log_udp(f'Received {msg}')
            if msg == "1":
                callback()


def callback():
    log_udp("Callback called")
    global callback_
    callback_()


def listen_forever(callback):
    global callback_

    log_udp("Listening on port 6969")
    listen_addr = ('0.0.0.0', 6969)

    callback_ = callback

    socketserver.UDPServer.allow_reuse_address = True 

    serverUDP = socketserver.UDPServer(listen_addr, UDPHandler)
    log_udp("Socket initialised, serving forever")
    serverUDP.serve_forever()
