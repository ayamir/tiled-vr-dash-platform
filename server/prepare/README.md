# 用于将一个全景视频分割成多个分块，每个分块使用dash来支持自适应播放 

## 一、使用FFmpeg将视频分割成多个分块

- 使用FFmpeg的videofilter能力

``` bash
ffmpeg -i input.mp4 -vf crop=<width>:<height>:<x>:<y> output.mp4 -y
# -i 输入
# -vf video filter
# width: 输出视频的宽度
# height：输出视频的高度
# x: 切割视频的参照起点x坐标
# y: 分割视频的参照起点y坐标
```

## 使用Python执行命令

### subporcess 模块
- 推荐采用subprocess来执行系统命令
- subprocess 模块首先推荐使用的是它的 run 方法，更高级的用法可以直接使用 Popen 接口。

``` python
# 构造函数
class subprocess.Popen(args, bufsize=-1, executable=None, stdin=None, stdout=None, stderr=None, 
preexec_fn=None, close_fds=True, shell=False, cwd=None, env=None, universal_newlines=False, 
startupinfo=None, creationflags=0,restore_signals=True, start_new_session=False, pass_fds=(),
*, encoding=None, errors=None)

# args：shell命令，可以是字符串或者序列类型（如：list，元组）
# bufsize：缓冲区大小。当创建标准流的管道对象时使用，默认-1。
    # 0：不使用缓冲区
    # 1：表示行缓冲，仅当universal_newlines=True时可用，也就是文本模式
    # 正数：表示缓冲区大小
    # 负数：表示使用系统默认的缓冲区大小。
# stdin, stdout, stderr：分别表示程序的标准输入、输出、错误句柄
# preexec_fn：只在 Unix 平台下有效，用于指定一个可执行对象（callable object），它将在子进程运行之前被调用
# shell：如果该参数为 True，将通过操作系统的 shell 执行指定的命令。
# cwd：用于设置子进程的当前目录。
# env：用于指定子进程的环境变量。如果 env = None，子进程的环境变量将从父进程中继承。

# 返回Popen对象，通过该对象，能够与子进程通信

p = subprocess.Popen(['ls', '-cl']) # 创建一个子进程来执行命令
p.poll()   # 检查进程是否终止，如果终止返回 returncode，否则返回 None。
p.wait(timeout) # 等待子进程终止。
p.communicate(input,timeout) # 和子进程交互，发送和读取数据。
p.send_signal(singnal) # 发送信号到子进程 。
p.terminate() # 停止子进程,也就是发送SIGTERM信号到子进程。
p.kill() # 杀死子进程。发送 SIGKILL 信号到子进程。

```
