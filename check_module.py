#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 检测import是否进行导入
print("""非常抱歉,至今没有找到pip instal pycurl的直接安装解决方法
Win用户您可以使用我们安提供的地址: https://github.com/waidinsamkeit/Dns-curl
本次程序仅仅监测dnspython模块
""")
import os
try:
    import time
    import sys
    import pycurl
    import dns.resolver
except ImportError:
    print("Module does not exist, installing for you")
    installs = os.system("pip install dnspython ")
    print("Install Successfuly")
else :
    print("依赖环境监测完成")
