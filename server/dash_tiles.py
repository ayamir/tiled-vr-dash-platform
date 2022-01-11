import cmder
import utils
import os
from pathlib import Path


def dash_mpd(video_output_dir: str) -> None:
    dirs = utils.get_dirs_path_in_path(video_output_dir)
    for dirpath in dirs:
        cmder.infOut("Current video directory is " + dirpath)
        # 生成base_dash.mpd
        tile_dirs = utils.get_dirs_path_in_path(dirpath)
        # Fragment all tiles
        video_list = list(Path(dirpath).rglob("*.mp4"))
        for video in video_list:
            video = str(video)
            if video.find("-fragmented") == -1:
                fragmented_video = video.replace(".mp4", "-fragmented.mp4")
                cmder.runCmd(f"mp4fragment {video} {fragmented_video}")
                os.remove(video)

        for tile_dir in tile_dirs:
            cmder.infOut("Current tile directory is " + tile_dir)
            tile_L0_path = os.path.join(tile_dir, "L0-fragmented.mp4")
            tile_L1_path = os.path.join(tile_dir, "L1-fragmented.mp4")
            # 生成每个tile的两种版本的mpd
            out_path = os.path.join(tile_dir, "output")
            cmder.runCmd(
                f"mp4dash --profiles=on-demand {tile_L1_path} {tile_L0_path} -o {out_path}"
            )
