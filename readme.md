## 平台设计

1. 视频编码选择：H.264
2. 视频投影格式：ERP
3. 视频分包传输：[DASH+HTTP/2(待看)](https://dl.acm.org/doi/10.1145/2736084.2736088)
4. Tile 划分方式：Static or [Dynamic(待看)](https://dl.acm.org/doi/10.1145/3123266.3123339)
5. Viewport 依赖
6. 视频内容无关

### 服务端

1. 将视频转换成 OMAF 兼容格式：[OMAF File Creation tools](https://github.com/fraunhoferhhi/omaf.js#file-creation-for-hevc-based-viewport-dependent-omaf-video-profile-with-mcts-hevc-tiles)

2. 划分 tile、确定不同质量等级：MP4Box、ffmpeg

   参考资料：

   1. [MPEG-DASH only with ffmpeg](https://blog.infireal.com/2018/04/mpeg-dash-with-only-ffmpeg/)：没有划分 tile
   2. [MPEG-DASH example](https://github.com/sanlengjingvv/mpeg-dash-sample)：没有划分 tile
   3. [Advanced Transport Options for DASH: QUIC and HTTP/2](https://bitmovin.com/advanced-transport-options-dash-quic-http2/)
   4. [Nodejs http2 doc](http://nodejs.cn/api/http2.html#server-side-example)
   5. [MP4Box](https://github.com/gpac/gpac/wiki/MP4Box)

3. 推流服务器：[Node-Media-Server](https://github.com/illuspas/Node-Media-Server)

### 客户端

1. 接近全部功能的播放器：[omaf.js](https://github.com/fraunhoferhhi/omaf.js)，依托论文：[ACM MMsys 19](https://dl.acm.org/doi/10.1145/3304109.3323835)
