#!/usr/bin/env python3
# coding: utf-8
from datetime import datetime

DAY_MILL_TIME = 1 * 24 * 60 * 60


def pre_day(count):
    now_time = datetime.now().timestamp()
    time = now_time - count * DAY_MILL_TIME
    date = datetime.fromtimestamp(time)
    return date


def pre_day_str(count):
    date = pre_day(count)
    s = date.__format__('%y%m%d')
    return s
