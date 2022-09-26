#!/usr/bin/python3

from Mailer import Mailer
from env import sender, password, receivers
import message as msg
from ReceiveUDP import listen_forever


def handle_alarm():
    print("handled alarm")

def alarm():
    mailer = Mailer(sender, password, receivers, server_host="smtp.gmail.com", server_port=465)
    mailer.send_mail(msg.get_formatted_msg())

if __name__ == "__main__":
    listen_forever(handle_alarm)
