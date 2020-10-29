# 一个建立自解析的Dns微弱项目

> 很简单的一个网站解析速度查询
> 来源于Amo大脑的产品  

# 邮箱

Email：ailunbolinkenasi@gmail.com
培训演练代码

[![forthebadge](https://forthebadge.com/images/badges/built-with-love.svg)](https://forthebadge.com)[![forthebadge](https://forthebadge.com/images/badges/uses-git.svg)](https://forthebadge.com)[![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)](https://forthebadge.com)

## 1.部署开始

### Windows用户

https://download.lfd.uci.edu/pythonlibs/x2tqcw5k/cp34/pycurl-7.43.1-cp34-cp34m-win_amd64.whl

并且将文件重命名为 `pycurl-7.43.1-cp37-abi3-win_amd64.whl`然后放到桌面

此方法只针对于Python3.x 由于官网已经把pycurl换成tar.gz了
所以直接pip install pycurl 会报错
我现在正在尝试把pycurl进行编译集成

```cmd
 pip install .\Desktop\pycurl-7.43.1-cp37-abi3-win_amd64.whl 
```

```cmd
pip debug --verbose # 查看pip支持的版本
```
