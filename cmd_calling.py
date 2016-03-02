from subprocess import Popen

if __name__ == "__main__":
    cmd = "notepad.exe cmd_calling.py"
    for i in range(10):
        Popen(cmd)
