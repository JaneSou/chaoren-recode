# -*- coding: utf-8-*-
"""
Mic.class 处理与麦克风和扬声器的所有交互
"""
import os
import logging
import ctypes

from bin import chaoren_path
from . import config

class Mic:
    speechRc =  None
    speechRc_persona = None

    def __init__(self, speaker, passive_stt_engine, active_stt_engine):
        """
        初始化 pocketsphinx 实例
        :param speaker:处理独立于平台的音频输出
        :param passive_stt_engine:当chaoren处于离线时所执行的stt
        :param active_stt_engine:当chaoren处于活跃状态时所用的stt
        """
        self.robot_name = config.get( 'robot_name_cn', u'超人')
        self._logger = logging.getLogger(__name__)
        self.speaker = speaker
        self.passive_stt_engine = passive_stt_engine
        self.active_stt_engine = active_stt_engine
        self.chaoren_path = chaoren_path
        self._logger.info("正在初始化 PyAudio" +
                          "在此过程中弹出的 ALSA 错误消息" +
                          "可以被忽略")
        try:
            asound = ctypes.cdll.LoadLibrary('libasound.so.2')
