
# ！/usr/bin/env python

# -*-coding:utf-8-*-

"""

@Author  : xiaofeng

@Time    : 2018/12/25 10:26

@Desc : Less interests,More interest.

@Project : python_appliction

@FileName: you-get.py

@Software: PyCharm

@Blog    ：https://blog.csdn.net/zwx19921215

"""

import sys

import you_get

 

 

def download(url, path):

    sys.argv = ['you-get', '-o', path, url]

    you_get.main()

 

 

if __name__ == '__main__':

    # 视频网站的地址

    url = 'https://v.qq.com/x/cover/5x2qc4mq9ctyu10/u0025rbc0jj.html'

    # 视频输出的位置

    path = 'G:/download'

    download(url, path)
