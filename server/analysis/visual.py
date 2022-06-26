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

    timeline = []
    for i in range(len(bufferLevelsList[0])):
        timeline.append(i)

    colors = iter([cm.tab20(i) for i in range(20)])

    for i in range(TILE_NUM):
        plt.plot(timeline,
                 bufferLevelsList[i],
                 label=("Tile-" + str(i + 1)),
                 color=next(colors))

    plt.title("BufferLevel Chart")
    plt.xlabel("Time")
    plt.xticks(ticks=timeline)
    plt.ylabel("BufferLevels")
    plt.grid(True)
    plt.legend(loc="center left", bbox_to_anchor=(1, 0.5))
    plt.savefig("buffer.png")


def drawBitrate():
    bitratesList = []
    for item in statistics:
        bitrates = item["bitrates"]
        bitratesList.append(bitrates)

    timeline = []
    for i in range(len(bitratesList[0])):
        timeline.append(i)

    colors = iter([cm.tab20(i) for i in range(20)])

    for i in range(TILE_NUM):
        plt.plot(timeline,
                 bitratesList[i],
                 label=("Tile-" + str(i + 1)),
                 color=next(colors))

    plt.title("Bitrate Chart")
    plt.xlabel("Time")
    plt.xticks(ticks=timeline)
    plt.ylabel("Bitrate")
    plt.grid(True)
    plt.legend(loc="center left", bbox_to_anchor=(1, 0.5))
    plt.savefig("bitrate.png")


def drawFrameRate():
    frameRatesList = []
    for item in statistics:
        frameRates = item["frameRates"]
        frameRatesList.append(frameRates)

    timeline = []
    for i in range(len(frameRatesList[0])):
        timeline.append(i)

    colors = iter([cm.tab20(i) for i in range(20)])

    for i in range(TILE_NUM):
        plt.plot(timeline,
                 frameRatesList[i],
                 label=("Tile-" + str(i + 1)),
                 color=next(colors))

    plt.title("FrameRate Chart")
    plt.xlabel("Time")
    plt.xticks(ticks=timeline)
    plt.ylabel("FrameRate")
    plt.grid(True)
    plt.legend(loc="center left", bbox_to_anchor=(1, 0.5))
    plt.savefig("frameRate.png")


def drawTileSequence():
    f = open("sequence.json")
    sequence = json.load(f)
    for item in sequence:
        print(item)
    print(len(sequence))


if __name__ == "__main__":
    choice = sys.argv[1]
    choice = eval(choice)
    if choice == 0:
        drawBufferLevel()
    elif choice == 1:
        drawBitrate()
    elif choice == 2:
        drawFrameRate()

    drawTileSequence()