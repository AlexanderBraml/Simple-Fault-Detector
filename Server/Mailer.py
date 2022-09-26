import smtplib, ssl

class Mailer():
    def __init__(self, sender, password, receivers, server_host="smtp.gmail.com", server_port=465):
        self.server_host = server_host
        self.server_port = server_port
        self.sender = sender
        self.password = password
        self.receivers = receivers
    
    def send_mail(self, msg):
        context = ssl.create_default_context()

        print("Starting to send")
        with smtplib.SMTP_SSL(self.server_host, self.server_port, context=context) as server:
            
            server.login(self.sender, self.password)
            for idx, receiver in enumerate(self.receivers[0]):
                msg = msg.replace('RECEIVERNAME', self.receivers[0][idx])
                msg = msg.replace('RECEIVERMAIL', receiver)
                server.sendmail(self.sender, receiver, msg)
                print("Sent e-mail " + str(idx + 1))
