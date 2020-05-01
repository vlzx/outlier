# Outlier

HTTP-to-SOCKS Proxy / GeoIP Filter

HTTP转SOCKS代理 / GeoIP分流

## 配置

```json
# ./resource/config.json
{
  "LISTEN_PORT": 8080,
  "PROXY_PORT": 1080
}
```

LISTEN_PORT：HTTP代理端口

PROXY_PORT：SOCKS5代理端口

## 运行

### 操作系统

- [x] Windows
- [ ] Linux
- [ ] Mac OS

### Windows

Power Shell（以管理员身份运行）

```shell
> cd /path/to/Outlier

> ./main.exe --startup=auto install

> ./main.exe start
```

Outlier作为Windows服务被配置为开机时自动启动，并且在Windows运行期间持续在后台运行。
