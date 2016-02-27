import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def send_email(conf, subject, body):
    from_addr = conf['fromEmail']
    to_addr = conf['toEmail']
    password = conf['password']

    msg = MIMEMultipart()
    msg['From'] = from_addr
    msg['To'] = to_addr
    msg['Subject'] = subject

    msg.attach(MIMEText(body, 'plain'))

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(from_addr, password)
    text = msg.as_string()
    server.sendmail(from_addr, to_addr, text)
    server.quit()


if __name__ == '__main__':
    configuration = {"fromEmail": "kristo.koert@gmail.com",
                     "toEmail": "timo@tdl.ee",
                     "password": ""}

    send_email(configuration, "Subject!", "Body!")
