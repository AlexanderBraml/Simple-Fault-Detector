import smtplib, ssl
from logger import log

class Mailer():
    def __init__(self, sender, password, receivers, server_host="smtp.gmail.com", server_port=465):
        self.server_host = server_host
        self.server_port = server_port
        self.sender = sender
        self.password = password
        self.receivers = receivers
    
    def send_mail(self, msg):
        context = ssl.create_default_context()

        log("Starting to send e-mails")
        with smtplib.SMTP_SSL(self.server_host, self.server_port, context=context) as server:
            
            server.login(self.sender, self.password)
            log("Login to smtp server successfull")
            for idx, receiver in enumerate(self.receivers[0]):
                msg = msg.replace('RECEIVERNAME', self.receivers[0][idx])
                msg = msg.replace('RECEIVERMAIL', receiver)
                server.sendmail(self.sender, receiver, msg)
                log("Sent mail to " + receiver)
        log("Finished sending e-mails")
