import os
from threading import Timer

from flask import Flask, request
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app)
app.config["CORS_HEADERS"] = "Content-Type"

host = "10.112.79.143"
port = 5002
crt = "/etc/nginx/ssl/10.112.79.143.crt"
key = "/etc/nginx/ssl/10.112.79.143.key"
cnt = 0
f = open("./4g/4.txt", "r")
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


@app.route("/control_start", methods=["POST"])
@cross_origin()
def control_start():
    if request.method == "POST":
        t = Timer(1, control_bandwidth, args=(lines,))
        t.start()
        return "200"


@app.route("/control_stop", methods=["POST"])
@cross_origin()
def control_stop():
    if request.method == "POST":
        global t
        t.cancel()
        return "200"


if __name__ == "__main__":
    app.run(debug=True, host=host, port=port, ssl_context=(crt, key))
