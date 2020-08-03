# -*- coding: utf-8 -*-
# @Author: Feng Heliang
# @Date:   2020-07-21 18:15:21
# @Last Modified by:   Feng Heliang
# @Last Modified time: 2020-07-22 11:43:37
import logging


class MyLogger():
    """日志类    
    """
    _instance = None    

    @classmethod
    def instance(cls) -> 'MyLogger':
        """Singleton instance (this prevents com creation on import)."""
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance

    def __init__(self):
        """初始化Logger
        """
        self.logger = logging.getLogger()
        # 设置日志输出等级
        self.logger.setLevel(logging.INFO)

        # 创建输出格式

        formatter = logging.Formatter(
            '%(asctime)s %(levelname)s %(name)s %(message)s')
        # 输出到文件
        fh = logging.FileHandler('log.txt', mode='w', encoding='utf8')
        fh.setFormatter(formatter)
        self.logger.addHandler(fh)

        # 输出到控制台
        sh = logging.StreamHandler()
        sh.setFormatter(formatter)
        self.logger.addHandler(sh)
