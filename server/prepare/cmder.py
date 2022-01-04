import subprocess


def redStr(str):
    return ' \033[1;31m ' + str + ' \033[0m '


def greenStr(str):
    return ' \033[1;32m ' + str + ' \033[0m '


def yelloStr(str):
    return ' \033[1;33m ' + str + ' \033[0m '


def buleStr(str):
    return ' \033[1;34m ' + str + ' \033[0m '


def errorOut(str):
    print(redStr('[Error]: ' + str))


def warningOut(str):
    print(yelloStr('[Warning]: ' + str))


def successOut(str):
    print(greenStr('[Success]: ' + str))


def infOut(str):
    print(buleStr('[Info]: ' + str))


def runCmd(command):
    infOut(command)
    subp = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE)
    res = subp.communicate()
    if subp.poll() == 0:
        print(res[0])
        successOut(command)
        return 0
    else:
        print(res[0])
        errorOut(command)
        return -1
