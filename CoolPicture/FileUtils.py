#!/usr/bin/env python3
# coding: utf-8

SAVE_FILE_PATH = '/home/wuhaojie/Wallpaper/CoolPicture/ECY/'


def save_file(file_name, content):
    with open(SAVE_FILE_PATH + file_name, 'wb') as file:
        file.write(content)
