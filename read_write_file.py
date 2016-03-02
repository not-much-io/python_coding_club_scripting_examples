def write_stuff():
    with open("test_file", "w+") as write_file:
        for i in range(10):
            write_file.write("Going to file!\n")


def read_stuff():
    with open("test_file", "r") as read_file:
        for line in read_file.readlines():
            print(line)


if __name__ == "__main__":
    write_stuff()
    read_stuff()
