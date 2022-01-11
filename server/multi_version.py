import cmder
import os
import shutil
import utils
from utils import TILE_HEIGHT
from utils import TILE_WIDTH


def process(
    video_path: str, width: float, height: float, output_path: str, mark: str
) -> None:
    res = cmder.runCmd(
        f"ffmpeg -i {video_path} \
        -vf scale={width}:{height},drawtext=fontcolor=white:fontsize=40:text='{mark}':x=10:y=10 \
        {output_path} -y"
    )
    if res == -1:
        os._exit(-1)


def transcode(workspace_dir: str) -> None:
    video_dirs = utils.get_dirs_in_path(workspace_dir)
    if len(video_dirs) != 1:
        print(f"There are {len(video_dirs)} video directories in path {workspace_dir}")
    else:
        print(f"There is {len(video_dirs)} video directory in path {workspace_dir}")

    for video_dir in video_dirs:
        video_dir = workspace_dir + video_dir
        cmder.infOut(f"Current video_dir is {video_dir}")
        tiled_video_root_dir = video_dir + "/tile_temp/"
        tiles = utils.get_files_in_path(tiled_video_root_dir)
        if len(tiles) == 0:
            cmder.errorOut(f"There are no tiles in {tiled_video_root_dir}")
        else:
            for tile_name in tiles:
                video_path = os.path.join(tiled_video_root_dir, tile_name)
                output_dir = os.path.join(video_dir, tile_name.replace(".mp4", ""))
                utils.create_dir(output_dir)
                process(
                    video_path,
                    TILE_WIDTH,
                    TILE_HEIGHT,
                    os.path.join(output_dir, "L1.mp4"),
                    f'{tile_name.replace(".mp4", "").replace("_","-")}-L1',
                )
                process(
                    video_path,
                    TILE_WIDTH / 2,
                    TILE_HEIGHT / 2,
                    os.path.join(output_dir, "L0.mp4"),
                    f'{tile_name.replace(".mp4", "").replace("_","-")}-L0',
                )
            shutil.rmtree(tiled_video_root_dir)
