#!/usr/bin/python3

from Mailer import Mailer
from env import sender, password, receivers
import message as msg
from ReceiveUDP import listen_forever
from time import time
from logger import log


last_alarm = 0
next_alarm_earliest = 0


def current_seconds():
    return int(time())


def handle_alarm():
    global next_alarm_earliest

    if current_seconds() > next_alarm_earliest:
        log("Alarm triggered")
        alarm()


def alarm():
    global next_alarm_earliest, last_alarm
    last_alarm = current_seconds()
    next_alarm_earliest = last_alarm + 60 * 60
    print(current_seconds(), "ALARM")
    mailer = Mailer(sender, password, receivers, server_host="smtp.gmail.com", server_port=465)
    mailer.send_mail(msg.get_formatted_msg())


if __name__ == "__main__":
    log("Starting server")
    listen_forever(handle_alarm)
