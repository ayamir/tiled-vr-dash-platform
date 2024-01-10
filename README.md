## 平台设计

1. 视频编码选择：H.264
2. 视频投影格式：ERP
3. 视频分包传输：Dash
4. Tile划分方式：静态划分
5. Viewport依赖
6. 视频内容无关

## 服务端

`stream`: 负责原始视频的切分、转码并转换成dash兼容的格式
`vp`: 使用基于轨迹的Viewport预测
`emulate`: 使用现网数据和tc命令进行带宽模拟
`analysis`: 使用客户端传回的`json`数据进行分析、绘图

## 客户端

`react-xrplayer`: 可以通过PC接入的观看平台，不支持VP预测
`webxr-player`: 可以通过VR头显(如:Meta Quest)的浏览器访问接入的全景视频播放客户端，支持VP预测
