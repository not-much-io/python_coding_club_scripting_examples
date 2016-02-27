import sys
from datetime import datetime
import time
import re

LIST_OF_ARGS = ['--start', '--interval', '--help']
HELP_DICT = {
    '--start' : 'Parameters are hours and minutes. Example:" --start 17:45 " script starts once on 17:45.',
    '--interval' : 'Parameters are minutes. Example:" --interval 130 " script starts in intervals after 130 minutes.',
    '--help' : 'Returns definitions and examples of arguments.'
            }

# ToDo: if user inserts '--interval' before '--start' then start argument is not read.

def parse_arguments():
    args = sys.argv
    args.pop(0) # remove file name
    used_args = []

    # No arguments
    if len(args) == 0:
        print("Starting script")
        return

    # Iterating over arguments
    i = 0
    while i < len(args):

        current_argument = args[i]

        if current_argument in LIST_OF_ARGS:

            # If argument is already used
            if current_argument in used_args:
                raise ValueError("You have already used this argument: %s" % (current_argument))

            # If argument is --help
            if current_argument == '--help':
                argument_parameter_check(current_argument, "")
                used_args.append(current_argument)

            # If argument is anything else
            else:
                argument_parameter_check(current_argument, args[i+1])
                used_args.append(current_argument)
                i += 1  # skip to next flag

        else:
            raise ValueError("Expected an argument like %s: , got %s" % (LIST_OF_ARGS, current_argument))

        i += 1


def argument_parameter_check(argument, parameter):

    if argument == '--help':

        print("Definition of arguments")
        print_dict(HELP_DICT)

    elif argument == '--start':

        if is_time(parameter):
            run_at_x_once(parameter)

    elif argument == '--interval':

        if is_number(parameter):
            run_every_x_interval(parameter)
    else:

        print("You shouldn't ever get here.")


def print_dict(x):

    for k, v in x.items():
        print(k + " " + v)


def is_number(x):

    x = int(x)

    if x <= 0 :
        raise TypeError("Expected whole number, got %s" % (x))

    return True


def is_time(x):

    pattern = re.compile("^(2[0-3]|[01]?[0-9]):([0-5]?[0-9])$")

    if pattern.match(x):
        return True
    else:
        raise TypeError("Expected time in format 22:09, got %s" % (x,))


def run_at_x_once(given_time):

    datetime_now = datetime.now()
    current_time = "{0}:{1}".format(datetime_now.hour, datetime_now.minute)

    while given_time != current_time:
        datetime_now = datetime.now()
        current_time = "{0}:{1}".format(datetime_now.hour, datetime_now.minute)

    print("We have reached your start time. Time: " + current_time + " now we can do whatever you want.")


def run_every_x_interval(interval):

    while True:
        interval = int(interval)
        time.sleep(interval * 60)
        print("Interval reached.")


if __name__ == "__main__":
    parse_arguments()