import smtplib
import traceback
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

class mailer(object):

    def __init__(self, config):
        self.config = config

    def send(self, content):
        try:
            server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
            server.ehlo()
            server.login(self.config.username, self.config.password)

            msg = MIMEMultipart('alternative')
            msg['Subject'] = "/".join(self.config.apps) + " User Interface Updates?!"
            msg['From'] = self.config.username
            msg['To'] = ", ".join(self.config.to)
            part2 = MIMEText(content, 'html')
            msg.attach(part2)

            print 'sending the nag!'
            server.sendmail(self.config.username, self.config.to
            , msg.as_string())
            server.close()
        except:
            traceback.print_exc()
