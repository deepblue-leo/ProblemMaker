# -*- coding: utf-8 -*-
# @Author: Heliang
# @Date:   2020-07-31 21:06:44
# @Last Modified by:   Heliang
# @Last Modified time: 2020-08-02 12:39:55
from logger import MyLogger as mlog
import random
import math
import os
import datetime


class binomol_problem_maker():
    """二项算式出题机
    """

    def __init__(self, positions, symbol):
        """初始化函数

        Args:
            postions (int): 创建几个数相乘的算式
            symbol (str): 计算符号
        """
        if positions <= 0:
            return
        else:
            self.positions = positions
            self.symbol = symbol

    def _make_a_participate(self, digits):
        """创建一个算式中的项

        Args:
            digits (int): 该项的位数

        Returns:
            int: -1 输入的位数不合法；其他 符合预期的值
        """
        return random.randint(math.pow(10, digits - 1), math.pow(10, digits) - 1)

    def _make_a_problem_str(self, digits):
        """产生一道题

        Args:
            digits (int): 计算项的位数

        Returns:
            str: 一道题的字符串
        """
        problem_str = f"{self._make_a_participate(digits)}"

        index = self.positions
        while index > 1:
            problem_str = problem_str + \
                f" {self.symbol} {self._make_a_participate(digits)}"

            index = index - 1
            if index == 1:
                problem_str = problem_str + " =    "

        return problem_str

    def yield_batch_problems(self, count, digits):

        index = count
        written_problem_count = 0
        filename = f"Question_{datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')}.txt"
        with open(filename, 'w+') as f:
            while index > 0:
                content = self._make_a_problem_str(digits)
                print(content)
                # mlog.instance().logger.info(self._make_a_problem_str(digits))
                f.writelines(content)
                index = index - 1
                written_problem_count = written_problem_count + 1
                if written_problem_count == 1:
                     f.writelines('\n')
                     written_problem_count = 0


if __name__ == '__main__':
    pmaker = binomol_problem_maker(2, 'x')
    # pmaker = binomol_problem_maker(2, "/")
    pmaker.yield_batch_problems(100, 2)
