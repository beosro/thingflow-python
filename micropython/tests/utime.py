# Copyright 2016 by MPI-SWS and Data-Ken Research.
# Licensed under the Apache 2.0 License.
"""Emuation for micropython's utime module
"""
from time import time, sleep

def ticks_ms():
    return int(round(time()*1000))

def sleep_ms(ms):
    sleep(ms/1000)

def ticks_diff(old, new):
    return new - old

