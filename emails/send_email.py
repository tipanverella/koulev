"""
    Simple email
"""
import smtplib
import json


def send_email(recipient, subject, text):
    """
    send text via email to recipient
    """
    with open("/home/tiparis/.gmail.credentials", "r") as json_io:
        creds = json.load(json_io)
    smtp_server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
    smtp_server.login(creds['username'], creds['password'])
    message = f"Subject: {subject}\n\n{text}"
    smtp_server.sendmail(creds['username'], recipient, message)
    smtp_server.close()

if __name__ == '__main__':
    send_email(
        "tipan.verella@gmail.com",
        "Test email numero 2 from Python",
        "Python di ou Bonjou!\nKouman ou ye?"
        )
