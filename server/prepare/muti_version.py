import cmder
import os
import utils
from utils import workspace_dir
from utils import TILE_HEIGHT
from utils import TILE_WIDTH


def process(video_path, width, height, output_path, mark):
    res = cmder.runCmd(
        f'ffmpeg -i {video_path} -vf scale={width}:{height},drawtext=fontcolor=white:fontsize=40:text=\'{mark}\':x=10:y=10 {output_path} -y')
    if res == -1:
        os._exit(-1)


def start_process():
    video_dirs = utils.get_dirs_in_path(workspace_dir)
    print(f'There are {len(video_dirs)} videos in path {workspace_dir}')
    for video_dir in video_dirs:
        tiled_video_root_dir = video_dir + "/tile_temp/"
        tiles = utils.get_files_in_path(tiled_video_root_dir)
        for tile_name in tiles:
            video_path = os.path.join(tiled_video_root_dir, tile_name)
            output_dir = os.path.join(video_dir, tile_name.replace(".mp4", ""))
            utils.create_dir(output_dir)
            process(
                video_path,
                TILE_WIDTH,
                TILE_HEIGHT,
                os.path.join(
                    output_dir,
                    "L1.mp4"),
                f'{tile_name.replace(".mp4", "").replace("_","-")}-L1')
            process(
                video_path,
                TILE_WIDTH / 2,
                TILE_HEIGHT / 2,
                os.path.join(
                    output_dir,
                    "L0.mp4"),
                f'{tile_name.replace(".mp4", "").replace("_","-")}-L0')


start_process()
