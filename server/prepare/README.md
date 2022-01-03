# 用于将一个全景视频分割成多个分块，每个分块使用 dash 来支持自适应播放

## 使用 FFmpeg 将视频分割成多个分块

- 使用 FFmpeg 的 videofilter 能力

```bash
ffmpeg -i input.mp4 -vf crop=<width>:<height>:<x>:<y> output.mp4 -y
# -i 输入
# -vf video filter
# width: 输出视频的宽度
# height：输出视频的高度
# x: 切割视频的参照起点x坐标
# y: 分割视频的参照起点y坐标
```
