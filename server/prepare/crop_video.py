import cmder
import os
import os.path
import utils
from utils import workspace_dir
from utils import video_src_dir
from utils import video_output_dir
from utils import TILE_HEIGHT
from utils import TILE_WIDTH


def get_video_list(dir_path):
    video_list = []
    for _, _, filenames in os.walk(dir_path):
        for filename in filenames:
            video_list.append(filename)
    return video_list


def create_output_dir(dir_path):
    path = dir_path
    path = path.rstrip("/")
    isExists = os.path.exists(path)
    if not isExists:
        os.makedirs(path)
    isExists = os.path.exists(path)
    if not isExists:
        return True
    else:
        return False


def crop(video_path, width, height, x, y, output_path):
    res = cmder.runCmd(
        f'ffmpeg -i {video_path} -vf crop={width}:{height}:{x}:{y} {output_path} -y')
    if res == -1:
        os._exit(-1)


def crop_video(video_dir, name, output_dir):
    # 为该视频创建总文件夹
    root_dir_name = name.replace(".mp4", "") + "/"
    res = utils.create_dir(output_dir + root_dir_name)
    # 生成Base低质量版本
    generate_base_video(video_dir + name, output_dir +
                        root_dir_name + "base.mp4")
    # 创建存储tile视频的文件夹
    tile_temp_dir = root_dir_name + "tile_temp/"
    res = utils.create_dir(output_dir + tile_temp_dir)

    if res:
        # 4x3
        for i in range(0, 4):
            for j in range(0, 3):
                x = TILE_WIDTH * i
                y = TILE_HEIGHT * j
                tile_name = "tile_" + str(i) + "_" + str(j) + ".mp4"
                output_path = output_dir + tile_temp_dir + tile_name
                crop(video_dir + name, TILE_WIDTH, TILE_HEIGHT,
                     x, y, output_path)


def generate_base_video(video_path, output_path):
    res = cmder.runCmd(
        f'ffmpeg -i {video_path} -vf scale=540x360 {output_path}')
    if res == -1:
        os._exit(-1)


def start_crop_videos(video_dir, output_dir):
    videoNames = get_video_list(workspace_dir)
    if (len(videoNames) == 0):
        print(cmder.redStr("ERROR: Not found video files"))
        return
    for name in videoNames:
        print("There are " + str(len(videoNames)) + " videos in this path")
        print("Crop " + video_dir + name)
        crop_video(video_dir, name, output_dir)


start_crop_videos(video_src_dir, video_output_dir)
