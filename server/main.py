import typing
import cmder
import os
import argparse

from utils import video_output_dir
from utils import video_src_dir
from crop_video import crop_videos
from dash_tiles import dash_mpd


def get_profile(exp: str) -> str:
    profile = ""
    if int(exp) == 1:
        profile = "live"
    elif int(exp) == 0:
        profile = "on-demand"

    return profile


def get_layout(exp: str) -> typing.Tuple:
    rows = int(exp.split("x")[0])
    cols = int(exp.split("x")[1])

    return rows, cols


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Crop Video and Dash Tiles.")
    parser.add_argument(
        "--profile",
        metavar="1",
        type=int,
        help="0 means 'VOD', 1 means 'LIVE', 1 is applied by default.",
        default=1,
        nargs="?",
    )
    parser.add_argument(
        "--layout",
        metavar="MxN",
        type=str,
        help="3x4 means crop video to 3x4 tiles, 3x4 is applied by dafault.",
        default="3x4",
        nargs="?",
    )
    args = parser.parse_args()
    profile = get_profile(args.profile)
    rows, cols = get_layout(args.layout)
    cmder.infOut(f"Profils is {profile}")
    cmder.infOut(f"Row is {rows}, col is {cols}")

    # 删除旧输出
    cmder.runCmd(f"bash -c 'rm -rf {video_output_dir}*'")
    # 切分tile
    crop_videos(video_src_dir, video_output_dir, rows, cols)
    # 生成dash资源和mpd
    dash_mpd(video_output_dir, profile=profile)
    # 拷贝新输出到文件服务器指定位置
    cmder.runCmd(f"bash -c 'rm -rf {os.getenv('HOME')}/public_html/*'")
    cmder.runCmd(f"bash -c 'cp -r {video_output_dir}* {os.getenv('HOME')}/public_html'")
