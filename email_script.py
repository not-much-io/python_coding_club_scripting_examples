import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def build_email(conf, subject, body):
    email = MIMEMultipart()
    email['From'] = conf['fromEmail']
    email['To'] = conf['toEmail']
    email['Subject'] = subject
    email.attach(MIMEText(body, 'plain'))
    return email.as_string()


def send_email(conf, email):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(conf['fromEmail'],
                 conf['password'])
    server.sendmail(conf['fromEmail'],
                    conf['toEmail'],
                    email)
    server.quit()


if __name__ == '__main__':
    configuration = {"fromEmail": "gatethor@gmail.com",
                     "toEmail": "",
                     "password": "Heimdall"}

    example_email = build_email(configuration, "Subject!", "Body!")
    send_email(configuration, example_email)
