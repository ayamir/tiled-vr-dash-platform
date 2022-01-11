import utils
from crop_video import crop_videos
from dash_tiles import dash_mpd

if __name__ == "__main__":
    # 切分tile
    crop_videos(utils.video_src_dir, utils.video_output_dir)
    # 生成dash资源和mpd
    dash_mpd(utils.video_output_dir)
