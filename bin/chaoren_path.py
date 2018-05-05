# -*- coding: utf-8-*-
import os

#项目主目录
APP_PATH = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), os.pardir))

#组件目录
DATA_PATH = os.path.join(APP_PATH, "data")
LIB_PATH = os.path.join(APP_PATH, "bin")
EXTRAS_PATH = os.path.join(APP_PATH, "extras")
TEMP_PATH = os.path.join(DATA_PATH, "temp")

#插件目录
LOGIN_PATH = os.path.join(EXTRAS_PATH, 'login')

#配置目录
CONFIG_PATH = os.path.expanduser(
    os.getenv('CHAOREN_CONFIG', '~/.chaoren')
)

CONTRIB_PATH = os.path.expanduser(
    os.getenv('CHAOREN_CONFIG', '~/.chaoren/contrib')
)

CUSTOM_PATH = os.path.expanduser(
    os.getenv('CHAOREN_CONFIG', '~/.chaoren/custom')
)

def config(*fname):
    return os.path.join(CONFIG_PATH, *fname)

def data(*fname):
    return  os.path.join(DATA_PATH, *fname)
