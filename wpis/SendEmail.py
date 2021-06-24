import smtplib
from email.message import EmailMessage
# @property
class Conf:
    def __init__(self):
        self.EMAIL_ADDRESS = "tp729864@gmail.com"
        self.EMAIL_PASSWORD = "vyovdacyozhmmgcb"
        self.port = 465
        self.stmp_serwer = "smtp.gmail.com"

class SendEmail(Conf):
    def EmailSettings(self, odbiorca):
        self.msg = EmailMessage()
        self.msg['Subject'] = 'Dziennik aktywności'
        self.msg['From'] = self.EMAIL_ADDRESS
        self.msg['To'] = odbiorca
        self.msg.set_content(''''
            Dzień dobry
            Załączam Twoje wpist w dzienniku aktywności.
            Dziękuję za skorzystanie z mojej apikacji :)
            
            Z poważaniem
        
        ''')
    def SendingAnEmail(self):
        with open('./Dziennik.docx', 'rb') as pdf:
            self.msg.add_attachment(pdf.read(), maintype='application', subtype='octet-stream', filename=pdf.name)

        with smtplib.SMTP_SSL(self.stmp_serwer, self.port) as smtp:
            smtp.login(self.EMAIL_ADDRESS, self.EMAIL_PASSWORD)
            smtp.send_message(self.msg)


if __name__ == '__main__':
    odbiorca = "wojtekm510@gmail.com"
    sendemail = SendEmail()
    sendemail.EmailSettings(odbiorca)
    sendemail.SendingAnEmail()




