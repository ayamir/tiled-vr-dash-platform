import sys
import json
import matplotlib.pyplot as plt
import matplotlib
from matplotlib import cm
from matplotlib.pyplot import figure

matplotlib.use("agg")
figure(figsize=(12, 6), dpi=96)

f = open("statistics.json")

statistics = json.load(f)

TILE_NUM = 15


def drawBufferLevel():
    bufferLevelsList = []
    for item in statistics:
        bufferLevels = item["bufferLevels"]
        bufferLevelsList.append(bufferLevels)

    frameList = []
    for i in range(len(bufferLevelsList[0])):
        frameList.append(i)

    colors = iter([cm.tab20(i) for i in range(20)])

    for i in range(TILE_NUM):
        plt.plot(frameList,
                 bufferLevelsList[i],
                 label=("Tile-" + str(i + 1)),
                 color=next(colors))

    plt.title("BufferLevel Chart")
    plt.xlabel("Frame")
    plt.ylabel("BufferLevels")
    plt.grid(True)
    plt.legend(loc="center left", bbox_to_anchor=(1, 0.5))
    plt.savefig("buffer.png")


def drawBitrate():
    bitratesList = []
    for item in statistics:
        bitrates = item["bitrates"]
        bitratesList.append(bitrates)

    frameList = []
    for i in range(len(bitratesList[0])):
        frameList.append(i)

    colors = iter([cm.tab20(i) for i in range(20)])

    for i in range(TILE_NUM):
        plt.plot(frameList,
                 bitratesList[i],
                 label=("Tile-" + str(i + 1)),
                 color=next(colors))

    plt.title("Bitrate Chart")
    plt.xlabel("Frame")
    plt.ylabel("Bitrate")
    plt.grid(True)
    plt.legend(loc="center left", bbox_to_anchor=(1, 0.5))
    plt.savefig("bitrate.png")


def drawFrameRate():
    frameRatesList = []
    for item in statistics:
        frameRates = item["frameRates"]
        frameRatesList.append(frameRates)

    frameList = []
    for i in range(len(frameRatesList[0])):
        frameList.append(i)

    colors = iter([cm.tab20(i) for i in range(20)])

    for i in range(TILE_NUM):
        plt.plot(frameList,
                 frameRatesList[i],
                 label=("Tile-" + str(i + 1)),
                 color=next(colors))

    plt.title("FrameRate Chart")
    plt.xlabel("Frame")
    plt.ylabel("FrameRate")
    plt.grid(True)
    plt.legend(loc="center left", bbox_to_anchor=(1, 0.5))
    plt.savefig("frameRate.png")


if __name__ == "__main__":
    choice = sys.argv[1]
    choice = eval(choice)
    if choice == 0:
        drawBufferLevel()
    elif choice == 1:
        drawBitrate()
    else:
        drawFrameRate()
