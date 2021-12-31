import cmder
import utils


def dash_all_videos(video_output_dir):
    dirs = utils.get_dirs_path_in_path(video_output_dir)
    for dirpath in dirs:
        print(dirpath)
        cmder.runCmd(
            f'MP4Box -dash 1000 -rap -profile dashavc264:onDemand L0.mp4#video L1.mp4#video L0.mp4#audio')


dash_all_videos(utils.video_output_dir)
