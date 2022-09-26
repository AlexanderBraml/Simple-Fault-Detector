#!/usr/bin/python3

from Mailer import Mailer
from env import sender, password, receivers
import message as msg


def alarm():
    mailer = Mailer(sender, password, receivers, server_host="smtp.gmail.com", server_port=465)
    mailer.send_mail(msg.get_formatted_msg())
