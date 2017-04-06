#!/usr/bin/env python3
# coding: utf-8
import json
from urllib import parse
from urllib import request
from ImageItemEntity import ImageItem

BASE_URL = 'http://apis.by-syk.com/cooldp.do'
KEY = '4270045430000000'


def get_image_info(day):
    """get the image info as json str with param of day
    :param day: str of the day
    """
    k = parse.urlencode([
        ('k', KEY),
        ('d', day),
        ('dd', 1),
    ])
    with request.urlopen(BASE_URL, k.encode('utf-8')) as http:
        data = http.read().decode('utf-8')
        d = json.loads(data)
        images = d['images'][0]
        author = images['author']
        title = images['title']
        url = images['url']
        return ImageItem(author, title, url)


def download_img(url):
    """ download picture with url
    :param url: url
    :return: binary content data
    """
    with request.urlopen(url) as http:
        return http.read()
