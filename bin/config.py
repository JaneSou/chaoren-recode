# -*- coding: utf-8-*-

import yaml
import logging
import os
from . import chaoren_path

_logger = logging.getLogger(__name__)
_config = {}

def init(config_name='profile.yml'):
    #如果config文件不存在则创建
    if not os.path.exists(chaoren_path.CONFIG_PATH):
        try:
            os.makedirs(chaoren_path.CONFIG_PATH)
        except OSError:
            _logger.error("创建路径失败: '%s'",chaoren_path.CONFIG_PATH,exc_info=True)
            raise

    #检查配置文件的可写性
    if not  os.access(chaoren_path.CONFIG_PATH,os.W_OK):
        _logger.critical("Con")
