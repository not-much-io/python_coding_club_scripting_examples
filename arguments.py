from sys import argv


def handle_arguments(raw_arguments):
    args = {}
    for i, arg in enumerate(raw_arguments):
        if "-" in arg:  # Is flag, ex. -a
            args[arg] = argv[i + 1]
    return args

if __name__ == "__main__":
    print("Raw arguments:\n", argv)
    formatted_args = handle_arguments(argv)
    print("Formatted arguments:\n", formatted_args)
