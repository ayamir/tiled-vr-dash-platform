import utils
import cmder
from crop_video import crop_videos
from multi_version import transcode
from dash_tiles import dash_mpd

if __name__ == "__main__":
    # 切分tile
    cmder.infOut("1. Begin to divide video to tiles...")
    crop_videos(utils.video_src_dir, utils.video_output_dir)
    # 转码
    cmder.infOut("2. Begin to transcode tiles bitrate...")
    transcode(utils.video_output_dir)
    # 生成dash资源和mpd
    cmder.infOut("3. Begin to generate mpd and dash files...")
    dash_mpd(utils.video_output_dir)
