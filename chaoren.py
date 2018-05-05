#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import os
import sys
import argparse
import logging
import threading

from bin import chaoren_path
from bin import config
# 添加环境变量到sys
sys.path.append(chaoren_path.LIB_PATH)

parse = argparse.ArgumentParser(description='助手语音控制中心')
parse.add_argument('--local', action='store_true', help='用文字代替麦克风输入')
parse.add_argument('--no-network-check', action='store_true', help='关闭网络连接检查')
parse.add_argument('--debug', action="store_true", help='展示debug消息')
parse.add_argument('--info', action='store_true', help= '展示info消息')
parse.add_argument('-v', '--verbose', action='store_true', help= '只输出日志，不写入日志文件')
args = parse.parse_args()

if args.local:
    from bin.local_mic import Mic
else:
    from bin.mic import Mic

class Chaoren(object):
    def __init__(self):
        self._logger = logging.getLogger(__name__)
        config.init()



if __name__ == "__main__":
    print('''
    
    毕业设计： 智能语音助手
    指导老师：沈翠新
    姓名：陈湛超
    学号：15240178
    班级：15计信3班
    
    ''')
