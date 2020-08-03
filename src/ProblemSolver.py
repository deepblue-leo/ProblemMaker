# -*- coding: utf-8 -*-
# @Author: Heliang
# @Date:   2020-08-02 13:41:25
# @Last Modified by:   Heliang
# @Last Modified time: 2020-08-02 15:05:24
import os
import sys
from logger import MyLogger as mlog


class ProblemSolver():
    def __init__(self, file_name):
        if len(file_name) == 0:
            return
        elif not os.path.isfile(file_name):
            return
        else:
            self._file_name = file_name

    def solve(self):
        answer_file_name = "Answer_" + self._file_name
        with open(answer_file_name, 'w+') as fp_answer:
            with open(self._file_name, 'r') as fp:
                lines = fp.readlines()

                for index, line in enumerate(lines):
                    line = line.replace('\n', '')
                    items = self._clear_line(line.split(' '))
                    item_count = len(items)

                    if item_count < 4:
                        mlog.instance().logger.error(
                            f"{self.__class__.__name__} {sys._getframe().f_code.co_name}: line {index} is invalid")

                    answer = self._calc_answer(items)
                    answer_str = u"answer " + f"{answer}"

                    
                    result_str = "    "

                    if item_count == 5:
                            # 带回答的情况
                        if int(items[4]) == answer:
                            result_str = u" right "
                            content = f"{line}\n"
                        else:
                            result_str = u" wrong "
                            content = f"{line}{result_str}{answer_str}\n"
                    fp_answer.write(content)
                    print(content)

    def _calc_answer(self, items: list):        
        signal = items[1]

        def multiple(part1: str, part2: str):
            return int(part1.strip()) * int(part2.strip())

        def division(part1: str, part2: str):
            return int(part1.strip()) / int(part2.strip())

        calc = {'x': multiple, '/': division}

        return calc[signal.strip()](items[0], items[2])

    def _clear_line(self, line: list):
        new_line = []
        for item in line:
            if len(str(item)) == 0 or str(item).find("\n") != -1:
                continue
            else:
                new_line.append(item)

        return new_line


if __name__ == "__main__":
    solver = ProblemSolver("Question_2020-08-02-12-39-59.txt")
    solver.solve()
