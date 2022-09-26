import time, datetime

msg = """From: Heizung <heizungsstoerung@braml.eu>
To: RECEIVERNAME <RECEIVERMAIL>
MIME-Version: 1.0
Content-type: text/html
Subject: STOERUNG

<h3>Die Heizung zeigt eine Stoerung an!</h1>
<h4>Stoerung war am [[DATE]] um [[TIME]]</h3>
"""

def get_date():
    return str(datetime.datetime.fromtimestamp(time.time()).strftime('%d.%m.%Y'))

def get_time():
    return str(datetime.datetime.fromtimestamp(time.time()).strftime('%H:%M'))

def get_formatted_msg():
    global msg
    msg = msg.replace('[[DATE]]', get_date())
    msg = msg.replace('[[TIME]]', get_time())
    return msg
