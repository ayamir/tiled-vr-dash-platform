import typing
import cmder
import os
import argparse

from utils import video_output_dir
from utils import video_src_dir
from crop_video import crop_videos
from dash_tiles import dash_mpd
from dash_tiles import generate_json


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
        "--https",
        metavar="0",
        type=int,
        help="1 means enable https. Default value is 0.",
        default=0,
        nargs="?",
    )
    parser.add_argument(
        "--json",
        metavar="0",
        type=int,
        help="1 means only generate json. Dafault value is 0.",
        default=0,
        nargs="?",
    )
    parser.add_argument(
        "--layout",
        metavar="MxN",
        type=str,
        help="6x4 means crop video to 6x4 tiles. Dafault value is 6x4.",
        default="6x4",
        nargs="?",
    )
    parser.add_argument(
        "--profile",
        metavar="1",
        type=int,
        help="0 means 'VOD'; 1 means 'LIVE'. Default value is 1.",
        default=1,
        nargs="?",
    )
    args = parser.parse_args()
    is_https = True if args.https == 1 else False
    profile = get_profile(args.profile)
    rows, cols = get_layout(args.layout)
    is_json = True if args.json == 1 else False
    cmder.infOut(f"Profils is {profile}")
    cmder.infOut(f"Row is {rows}, col is {cols}")

    # 生成客户端请求的 json 文件
    generate_json(is_https, rows, cols, video_output_dir)
    crop_videos(video_src_dir, video_output_dir, rows, cols, is_json)

    if not is_json:
        # 删除旧输出
        cmder.runCmd(f"bash -c 'rm -rf {video_output_dir}*'")
        # 切分tile
        crop_videos(video_src_dir, video_output_dir, rows, cols, False)
        # 生成 dash 资源和 mpd
        dash_mpd(video_output_dir, profile=profile)
        # 拷贝新输出到文件服务器指定位置
        cmder.runCmd(f"bash -c 'rm -rf {os.getenv('HOME')}/public_html/*'")
        cmder.runCmd(
            f"bash -c 'cp -r {video_output_dir}* {os.getenv('HOME')}/public_html'"
        )
