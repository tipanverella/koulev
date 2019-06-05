"""
    Markdown email
    ref: 
        - https://dbader.org/blog/python-send-email
        - https://gist.github.com/cleverdevil/8250082
"""
import smtplib
import json
import markdown
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def send_email(recipient, subject, text):
    """
    send markdown via email to recipient
    """
    with open("/home/tiparis/.gmail.credentials", "r") as json_io:
        creds = json.load(json_io)
    smtp_server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
    smtp_server.login(creds['username'], creds['password'])
    message = MIMEMultipart('alternative')
    message['To'] = recipient
    message['From'] = creds['username']
    message['Subject'] = subject
    message.attach(MIMEText(markdown.markdown(text), 'html'))
    smtp_server.sendmail(creds['username'], message['To'].split(','), message.as_string())
    smtp_server.close()

if __name__ == '__main__':
    send_email(
        "tipan.verella@gmail.com",
        "Test email numero 2 from Python",
        """# Yo Tipan!\n\n **Python** di ou Bonjou!\nKouman ou ye?"""
        )
