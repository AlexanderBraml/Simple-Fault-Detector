import smtplib, ssl
import time, datetime

from env import server_port, server_host, sender, password, receivers, names

message_orig = """From: Heizung <heizungsstoerung@braml.eu>
To: RECEIVERNAME <RECEIVERMAIL>
MIME-Version: 1.0
Content-type: text/html
Subject: STOERUNG

<h3>Die Heizung zeigt eine Stoerung an!</h1>
<h4>Stoerung war am DATUM um UHRZEIT</h3>
"""

def send_mails():
    context = ssl.create_default_context()

    print("Starting to send")
    with smtplib.SMTP_SSL(server_host, server_port, context=context) as server:
        get_date = lambda: str(datetime.datetime.fromtimestamp(time.time()).strftime('%d.%m.%Y'))
        get_time = lambda: str(datetime.datetime.fromtimestamp(time.time()).strftime('%H:%M'))
        server.login(sender, password)
        for idx, receiver in enumerate(receivers):
            message = message_orig
            message = message.replace('RECEIVERNAME', names[idx])
            message = message.replace('RECEIVERMAIL', receiver)
            message = message.replace('DATUM', get_date())
            message = message.replace('UHRZEIT', get_time())
            server.sendmail(sender, receiver, message)
            print("Sent e-mail " + str(idx + 1))
