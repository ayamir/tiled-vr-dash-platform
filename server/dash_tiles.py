import json
import cmder
import utils
import os
from pathlib import Path


def dash_mpd(video_output_dir: str, profile: str = "on-demand") -> None:
    dirs = utils.get_dirs_path_in_path(video_output_dir)
    for dirpath in dirs:
        cmder.infOut("Current video directory is " + dirpath)
        tile_dirs = utils.get_dirs_path_in_path(dirpath)

        # Fragment all mp4
        video_list = list(Path(dirpath).rglob("*.mp4"))
        for video in video_list:
            video = str(video)
            if video.find("-fragmented") == -1:
                fragmented_video = video.replace(".mp4", "-fragmented.mp4")
                cmder.runCmd(f"mp4fragment {video} {fragmented_video}")
                os.remove(video)

        # Generate base_dash.mpd
        base_path = os.path.join(dirpath, "base-fragmented.mp4")
        base_output_path = os.path.join(dirpath, "output")
        if os.path.exists(base_path):
            cmder.runCmd(
                f"mp4dash --profiles={profile} {base_path} -o {base_output_path}"
            )

        # Generate tiles mpd
        for tile_dir in tile_dirs:
            cmder.infOut("Current tile directory is " + tile_dir)
            tile_L0_path = os.path.join(tile_dir, "L0-fragmented.mp4")
            tile_L1_path = os.path.join(tile_dir, "L1-fragmented.mp4")
            out_path = os.path.join(tile_dir, "output")
            cmder.runCmd(
                f"mp4dash --profiles={profile} '{tile_L1_path}' '[type=video]{tile_L0_path}' -o {out_path}"
            )


def generate_json(
    rows: int,
    cols: int,
    video_output_dir: str,
    url_prefix: str = "http://localhost:80/~ayamir/070",
    fov: int = 100,
    is_rotate: bool = False,
    rotate_speed: float = 1.0,
    volume: int = 90,
    muted: bool = False,
) -> None:

    url_suffix = "/output/stream.mpd"

    res_urls = []
    res_url = {
        "type": "tiled-dash",
        "res_url": [url_prefix + url_suffix],
        "rows": rows,
        "cols": cols,
        "panoramic_type": "360",
        "radius": 500,
    }

    for i in range(cols):
        for j in range(rows):
            res_url["res_url"].append(
                url_prefix + "/tile_" + str(j) + "_" + str(i) + url_suffix
            )

    res_urls.append(res_url)
    obj = {
        "camera_fov": fov,
        "enable_auto_rotate": is_rotate,
        "auto_rotate_speed": rotate_speed,
        "volume": volume,
        "muted": muted,
        "res_urls": res_urls,
    }

    out_path = video_output_dir + "view-tiled.json"
    dest = os.getcwd() + "/../client/react-xrplayer/public/mock/view-tiled.json"
    with open(out_path, "w") as outfile:
        json.dump(obj, outfile)
        cmder.runCmd(f"mv {out_path} {dest}")
