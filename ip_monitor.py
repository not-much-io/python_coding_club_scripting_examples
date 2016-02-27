from time import sleep
from requests import get
from email_script import send_email_to_me
import socket


def get_ip():
    return get('https://api.ipify.org').text


if __name__ == '__main__':
    last_ip = "None, script just started."
    while True:
        curr_ip = get_ip()

        if curr_ip != last_ip:
            send_email_to_me("Ip changed on " + socket.gethostname() + ", new ip: " + curr_ip,
                             "Last ip was: " + last_ip)
            last_ip = curr_ip
            print("Sent new IP: ", curr_ip)
        else:
            print("ZZzz..")
            sleep(3600)
