import subprocess


def redStr(str: str):
    return ' \033[1;31m ' + str + ' \033[0m '


def greenStr(str: str):
    return ' \033[1;32m ' + str + ' \033[0m '


def yelloStr(str: str):
    return ' \033[1;33m ' + str + ' \033[0m '


def buleStr(str: str):
    return ' \033[1;34m ' + str + ' \033[0m '


def errorOut(str: str):
    print(redStr('[Error]: ' + str))


def warningOut(str: str):
    print(yelloStr('[Warning]: ' + str))


def successOut(str: str):
    print(greenStr('[Success]: ' + str))


def infOut(str: str):
    print(buleStr('[Info]: ' + str))


def runCmd(command: str):
    infOut(command)
    subp = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE)
    res = subp.communicate()
    if subp.poll() == 0:
        successOut(command)
        return 0
    else:
        errorOut(command)
        return -1
