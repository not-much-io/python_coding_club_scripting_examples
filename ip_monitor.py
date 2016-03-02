from time import sleep
from requests import get
from email_script import send_email_to
import socket


def get_ip():
    return get('https://api.ipify.org').text


if __name__ == '__main__':
    last_ip = "None, script just started."

    while True:
        curr_ip = get_ip()
        title = "Ip changed on " + socket.gethostname() + ", new ip: " + curr_ip
        body = "Last ip was: " + last_ip

        if curr_ip != last_ip:
            send_email_to("me", title, body)
            last_ip = curr_ip
            print("Sent new IP: ", curr_ip)
        else:
            sleep(3600)
