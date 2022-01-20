import typing
import math
import cmder
import os
import utils
from multi_version import transcode
from utils import workspace_dir


def get_video_list(dir_path: str) -> typing.List[str]:
    video_list = []
    for _, _, filenames in os.walk(dir_path):
        for filename in filenames:
            video_list.append(filename)
    return video_list


def create_output_dir(dir_path: str) -> bool:
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


def crop(
    video_path: str, width: int, height: int, x: int, y: int, output_path: str
) -> None:
    code, _ = cmder.runCmd(
        f"ffmpeg -i {video_path} -vf crop={width}:{height}:{x}:{y} {output_path} -y"
    )
    if code == -1:
        os._exit(-1)


def crop_video(video_dir: str, name: str, output_dir: str) -> None:
    # 为该视频创建总文件夹
    root_dir_name = name.replace(".mp4", "") + "/"
    res = utils.create_dir(output_dir + root_dir_name)
    output_root_dir = output_dir + root_dir_name
    argu = "'{print $2}'"
    _, video_width_str = cmder.runCmd(
        f"mp4info {video_dir + name} | grep Width | awk {argu}"
    )
    _, video_height_str = cmder.runCmd(
        f"mp4info {video_dir + name} | grep Height | awk {argu}"
    )
    tile_width = math.floor(int(video_width_str) / 4)
    tile_height = math.floor(int(video_height_str) / 3)
    base_width = tile_width + 120
    base_height = tile_height + 120
    cmder.infOut(f"tile width = {tile_width}")
    cmder.infOut(f"tile height = {tile_height}")
    cmder.infOut(f"base width = {base_width}")
    cmder.infOut(f"base height = {base_height}")

    # 生成Base低质量版本
    cmder.infOut("Begin to crop tile ...")
    generate_base_video(
        video_dir + name,
        base_width,
        base_height,
        output_dir + root_dir_name + "base.mp4",
    )

    # 创建存储tile视频的文件夹
    tile_temp_dir = root_dir_name + "tile_temp/"
    res = utils.create_dir(output_dir + tile_temp_dir)

    if res:
        # 4x3
        for i in range(0, 4):
            for j in range(0, 3):
                x = tile_width * i
                y = tile_height * j
                tile_name = "tile_" + str(i) + "_" + str(j) + ".mp4"
                output_path = output_dir + tile_temp_dir + tile_name
                crop(video_dir + name, tile_width, tile_height, x, y, output_path)
    else:
        cmder.errorOut("Create temp directory failed!")

    transcode(output_root_dir, tile_width, tile_height)


def generate_base_video(
    video_path: str, base_width: int, base_height: int, output_path: str
) -> None:
    code, _ = cmder.runCmd(
        f"ffmpeg -i {video_path} -vf scale={base_width}x{base_height} {output_path}"
    )
    if code == -1:
        os._exit(-1)


def crop_videos(video_dir: str, output_dir: str) -> None:
    video_names = get_video_list(workspace_dir)
    if len(video_names) == 0:
        cmder.redStr("ERROR: Not found video files")
        return
    else:
        ("There are " + str(len(video_names)) + " videos in this path")
    for name in video_names:
        cmder.infOut("Crop " + video_dir + name)
        crop_video(video_dir, name, output_dir)
