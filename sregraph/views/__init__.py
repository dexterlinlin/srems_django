#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'Administrator'
__mtime__ = '2019/4/3 0003'
"""
from bottle import Bottle

global btl
def initDynamicViews(bottle):
    btl = bottle

class SharedParams:

    @staticmethod
    def getBottle():
        return btl

def main(args=None, out=None):
    pass

if __name__ == '__main__':
    main()

