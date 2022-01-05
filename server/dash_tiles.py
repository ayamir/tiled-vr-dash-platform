import cmder
import utils
import os


def dash_mpd(video_output_dir: str) -> None:
    dirs = utils.get_dirs_path_in_path(video_output_dir)
    for dirpath in dirs:
        cmder.infOut("Current video directory is " + dirpath)
        # 生成base_dash.mpd
        base_video_path = os.path.join(dirpath, "base.mp4")
        base_mpd_path = os.path.join(dirpath, "base_dash.mpd")
        cmder.runCmd(
            f'MP4Box -dash 1000 -rap -profile dashavc264:onDemand {base_video_path} -out {base_mpd_path}')
        tile_dirs = utils.get_dirs_path_in_path(dirpath)
        for tile_dir in tile_dirs:
            cmder.infOut("Current tile directory is " + tile_dir)
            # 生成每个tile的两种版本的mpd
            tile_L0_path = os.path.join(tile_dir, "L0.mp4")
            tile_L1_path = os.path.join(tile_dir, "L1.mp4")
            out_mpd_path = os.path.join(tile_dir, "L1_dash.mpd")
            cmder.runCmd(
                f'MP4Box -dash 1000 -rap -profile dashavc264:onDemand {tile_L1_path} {tile_L0_path} -out {out_mpd_path}')
