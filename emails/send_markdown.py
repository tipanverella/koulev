"""
    Markdown email
    ref:
        - https://dbader.org/blog/python-send-email
        - https://gist.github.com/cleverdevil/8250082
"""
import os
import smtplib
import json
import subprocess

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import markdown


def send_email(recipient, subject, text):
    """
    send markdown via email to recipient
    """
    with open(os.path.expanduser("~/.gmail.credentials"), "r") as json_io:
        creds = json.load(json_io)
    smtp_server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
    smtp_server.login(creds['username'], creds['password'])
    message = MIMEMultipart('alternative')
    message['To'] = recipient
    message['From'] = creds['username']
    message['Subject'] = subject
    css = str(subprocess.check_output(['pygmentize', '-S', 'default', '-f', 'html']))
    html_content = markdown.markdown(
        text,
        extensions=[
            'extra',
            'fenced_code',
            'codehilite',
            'tables'])
    html_content = '<style type="text/css">'+css+'</style>'+html_content
    message.attach(MIMEText(html_content, 'html'))
    smtp_server.sendmail(creds['username'], message['To'].split(','), message.as_string())
    smtp_server.close()

if __name__ == '__main__':
    MYTEXT = """
# Yo Tipan!

**Python** di ou Bonjou!
    
Kouman ou ye?

Men yon ti code `python`
```python 
diksyone = dict([(k,v) for k,v in list_of_pairs])
```

Men yon ti `sql`
```sql
select *
from mytable
where my_condition
```

First Header  | Second Header
------------- | -------------
Content Cell  | Content Cell
Content Cell  | Content Cell
    """
    send_email(
        "tipan.verella@gmail.com",
        "Test email numero 3 from Python",
        MYTEXT
        )
