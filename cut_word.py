# -*- coding: utf-8 -*-
"""
# @Time    : 2018/1/20 下午9:20
# @Author  : zhanzecheng
# @File    : cut_word.py
# @Software: PyCharm
"""

import jieba
import re
import tqdm
from multiprocessing import Pool
seg_list = jieba.cut("我来到北京清华大学", cut_all=False)

with open('/Users/zhanzecheng/Desktop/wiki.zh.test.jian', 'r') as f, open('/Users/zhanzecheng/Desktop/train.txt', 'w', encoding='utf-8') as d:
    lines = f.readlines()
    for line in tqdm.tqdm(lines):
        line = line.replace(" ", "")
        removePun = re.compile('[a-z]')
        line = re.sub(removePun, "", line)
        removePun = re.compile('[A-Z]')
        line = re.sub(removePun, "", line)
        line = jieba.cut(line, cut_all=False)
        result = ""
        for da in line:
            result += da
            result += " "
        result = result[:-3] + '\n'
        d.write(result)