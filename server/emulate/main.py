import os
from threading import Timer

cnt = 0
f = open("./4g/5.txt", "r")
lines = f.readlines()


def control_bandwidth(lines: list):
    global t, cnt
    cnt += 1
    line = lines[cnt]
    arr = line.strip().split(" ")
    bandwidth = arr[1]
    os.system(
        f"tcset enp3s0 --direction outgoing --rate {bandwidth}Mbps --port 443 --overwrite"
    )
    os.system("tcshow enp3s0")
    if cnt < len(lines):
        t = Timer(1, control_bandwidth, args=(lines,))
        t.start()


if __name__ == "__main__":
    t = Timer(1, control_bandwidth, args=(lines,))
    t.start()
