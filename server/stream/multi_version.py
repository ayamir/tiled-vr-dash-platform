import typing
import math
import cmder
import os
import shutil
import utils


def calculate_wh(
    width: int, height: int, divisor1: int = 2, divisor2: int = 2
) -> typing.Tuple:
    w = math.floor(width / divisor1)
    h = math.floor(height / divisor2)

    if w % 2 == 0 and h % 2 == 0:
        return w, h
    if w % 2 == 0 and h % 2 != 0:
        return w, h + 1
    elif h % 2 == 0 and w % 2 != 0:
        return w + 1, h
    else:
        return w + 1, h + 1


def process(video_path: str, output_path: str, crf: int, mark: str) -> None:
    code, _ = cmder.runCmd(
        f"ffmpeg -i {video_path} \
                -crf {crf} -vf drawtext=fontcolor=white:fontfile='./assets/RobotoMono-Bold.ttf':fontsize=40:text='{mark}':x=10:y=10 \
        {output_path} -y"
    )
    if code == -1:
        os._exit(-1)


def transcode(video_dir: str) -> None:
    tiled_video_root_dir = os.path.join(video_dir, "tile_temp")
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
                os.path.join(output_dir, "L2.mp4"),
                25,
                f'{tile_name.replace(".mp4", "").replace("_","-")}-L2',
            )
            process(
                video_path,
                os.path.join(output_dir, "L1.mp4"),
                30,
                f'{tile_name.replace(".mp4", "").replace("_","-")}-L1',
            )
            process(
                video_path,
                os.path.join(output_dir, "L0.mp4"),
                45,
                f'{tile_name.replace(".mp4", "").replace("_","-")}-L0',
            )
        shutil.rmtree(tiled_video_root_dir)
