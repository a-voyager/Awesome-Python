#!/usr/bin/env python3
# coding: utf-8

import HttpHelper
from DateUtils import pre_day_str
from FileUtils import save_file

for i in range(100, 151):
    try:
        pre = pre_day_str(i)
        item = HttpHelper.get_image_info(pre)
        print(str(i) + ':  ' + item.title + '   ' + item.author + '   ' + item.url)
        content = HttpHelper.download_img(item.url)
        suffix = item.url[-4:]
        file_name = item.title + ' @' + item.author + suffix
        save_file(file_name, content)
    except:
        continue
