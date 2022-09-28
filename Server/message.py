import time, datetime
from env import msg


def get_date():
    return str(datetime.datetime.fromtimestamp(time.time()).strftime('%d.%m.%Y'))

def get_time():
    return str(datetime.datetime.fromtimestamp(time.time()).strftime('%H:%M'))

def get_formatted_msg():
    fmsg = msg.replace('[[DATE]]', get_date())
    fmsg = fmsg.replace('[[TIME]]', get_time())
    return fmsg
