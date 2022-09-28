import datetime, time
from os import times
from env import log_path, udp_log_path


def delete_udp_log():
    with open(udp_log_path, 'w') as f:
        f.write('')


def timestamp():
    return str(datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S'))


def add_timestamp(text):
    return f'{timestamp()} {text}'

def append_to_file(filename, text):
    with open(filename, 'a') as f:
        f.write(text + '\n')


def log(text):
    append_to_file(log_path, add_timestamp(text))


def log_udp(text):
    pass # append_to_file(udp_log_path, add_timestamp(text))
