## 平台设计

1. 视频编码选择：H.264
2. 视频投影格式：ERP
3. 视频分包传输：服务端使用 apache 作为文件服务器
4. Tile 划分方式：静态划分
5. Viewport 依赖
6. 视频内容无关

## 部署

### 服务端

1. 安装 `apache2` 服务器

   ```shell
   sudo apt install apache2
   ```

2. 配置 `apache2` 服务器，将下面内容复制到其配置文件的对应位置

   ```conf
   Header always set Access-Control-Allow-Origin "*"
   Header always set Access-Control-Allow-Methods "POST, GET, OPTIONS, DELETE, PUT"
   Header always set Access-Control-Allow-Headers "x-requested-with, Content-Type, origin, authorization, accept, client-security-token, Range"
   Header always set Access-Control-Expose-Headers "Content-Security-Policy, Location"
   Header always set Access-Control-Max-Age "600"
   ```

3. 启动 `apache2` 服务器

   ```shell
   sudo systemctl start apache2
   ```

### 客户端

1. 安装 `nginx` 服务器

   ```shell
   sudo apt install nginx
   ```

2. 配置 `nginx` 服务器

   ```shell
   cd /etc/nginx
   sudo mkdir -p ./servers && cd ./servers
   sudo touch player.conf
   sudo vim player.conf
   ```

   填入下面的内容

   ```conf
    server {
        listen       5555;
        server_name  player;
        autoindex on;
        root /opt/player;
        location / {
        }
    }
   ```

   编辑 `nginx.conf` ，在 `http` 开头的块中填入下面这行：

   ```conf
   include servers/*.conf
   ```

3. 进入 `react-xrplayer` 目录下执行：
   ```shell
   npm run build
   ```
4. 复制生成的 `build` 目录

   ```shell
   sudo mkdir -p /opt/player
   sudo cp -vr ./build /opt/player/react-xrplayer
   ```

5. 启动 `nginx` 服务器

   ```shell
   sudo systemctl start nginx
   ```

6. 检查结果

   打开浏览器（推荐 `chrome` ）,网址栏输入 `http://localhost:5555/react-xrplayer` 即可
