import sys
import cmder
import os

from utils import video_output_dir
from utils import video_src_dir
from crop_video import crop_videos
from dash_tiles import dash_mpd

if __name__ == "__main__":
    if len(sys.argv) == 1:
        cmder.errorOut("Please set arguments: 0 means 'VOD'; 1 means 'LIVE'")
    else:
        cmder.runCmd(f"bash -c 'rm -rf {video_output_dir}*'")
        if eval(sys.argv[1]) == 0:
            # 切分tile
            crop_videos(video_src_dir, video_output_dir)
            # 生成dash资源和mpd
            dash_mpd(video_output_dir)
        elif eval(sys.argv[1]) == 1:
            # 切分tile
            crop_videos(video_src_dir, video_output_dir)
            # 生成dash资源和mpd
            dash_mpd(video_output_dir, "live")
        cmder.runCmd(
            f"bash -c 'cp -r {video_output_dir}* {os.getenv('HOME')}/public_html'"
        )
