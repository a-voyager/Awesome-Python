#!/usr/bin/env python3
# coding: utf-8

import os

all_count = {}
include_suffix = ['py']


def dfs(p):
    """
    search for all sub files and directories
    :param p: the root path <string>
    """
    ll = os.listdir(p)
    for x in [p + i for i in ll]:
        if os.path.isdir(x):
            dfs(x + '/')
        if os.path.isfile(x):
            for sf in include_suffix:
                if os.path.splitext(x)[1] == '.' + sf:
                    length = count(x)
                    save_result(x, length, sf)
                    break


def save_result(path, length, key):
    """
    save file length
    :param path: the file
    :param length: the file line number
    :param key: the file tag
    """
    if key not in all_count:
        all_count[key] = length
    else:
        all_count[key] += length
    log(path + '   ' + str(length))


def count(p):
    """
    count the line number of the file
    :param p: the file path <string>
    :return: the count of lines
    """
    if not os.path.isfile(p):
        return
    with open(p) as f:
        try:
            l = f.readlines()
            cnt = len(l)
        except UnicodeDecodeError as e:
            log(e)
            return 0
        return cnt


def log(e):
    """
    debug log
    :param e: the message to print 
    """
    print(e)


if __name__ == '__main__':
    dfs('/home/wuhaojie/WorkSpace/Python/')
    print(all_count)
