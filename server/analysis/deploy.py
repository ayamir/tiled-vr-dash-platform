import os
from flask import Flask, request
from flask_cors import CORS, cross_origin
import numpy as np
import json
import cmder
import matplotlib

matplotlib.use("agg")
import matplotlib.pyplot as plt

app = Flask(__name__)
cors = CORS(app)
app.config["CORS_HEADERS"] = "Content-Type"

host = "10.112.79.143"
port = 5001
crt = "/etc/nginx/ssl/10.112.79.143.crt"
key = "/etc/nginx/ssl/10.112.79.143.key"

pi = np.pi
sin = np.sin
cos = np.cos

u = np.linspace(0, 2 * pi, 100)
v = np.linspace(0, pi, 100)
r = 1
x = r * np.outer(np.cos(u), np.sin(v))
y = r * np.outer(np.sin(u), np.sin(v))
z = r * np.outer(np.ones(np.size(u)), np.cos(v))


@app.route("/trace", methods=["POST"])
@cross_origin()
def trace_visual():
    if request.method == "POST":
        points = request.get_json()
        json_object = json.dumps(points)
        with open("trace.json", "w") as f:
            f.write(json_object)
        xs = points["x"]
        ys = points["y"]
        zs = points["z"]
        fig = plt.figure(facecolor="Black")
        ax = plt.axes(projection="3d")
        ax.set_facecolor("#1DD4AF")
        for i in range(len(xs)):
            xx = xs[i]
            yy = ys[i]
            zz = zs[i]
            ax.scatter(xx, yy, zz, color="k", s=20)
        plt.title("Viewpoint Trace")
        plt.savefig("trace.png")
        return "200"


@app.route("/statistics", methods=["POST"])
@cross_origin()
def statistics_visual():
    if request.method == "POST":
        statistics = request.get_json()
        json_object = json.dumps(statistics)
        with open("statistics.json", "w") as f:
            f.write(json_object)
        cmder.runCmd(
            "/home/ayamir/anaconda3/envs/vp-lstm/bin/python visual.py 0")
        cmder.runCmd(
            "/home/ayamir/anaconda3/envs/vp-lstm/bin/python visual.py 1")
        cmder.runCmd(
            "/home/ayamir/anaconda3/envs/vp-lstm/bin/python visual.py 2")
        return "200"


if __name__ == "__main__":
    app.run(debug=True, host=host, port=port, ssl_context=(crt, key))
