## 工作内容

1. 将 videos 目录下的所有视频进行划分
2. 将划分好的每个 tile 转码成两个质量版本
3. 为每个视频生成 dash 文件：mp4 和 mpd

## 依赖

1. [bento4](https://www.bento4.com/)

   直接下载二进制包即可，注意将其解压到`PATH`中

2. [ffmpeg](https://www.ffmpeg.org/)

   ```shell
   sudo apt install ffmpeg
   ```

## 用法

直接执行`main.py`即可

```shell
python3 main.py
```
