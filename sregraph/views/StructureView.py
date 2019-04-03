#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'Administrator'
__mtime__ = '2019/4/3 0003'
"""
from bottle import get, post, redirect, request, run, static_file, template, TEMPLATE_PATH
from sregraph.db import DBProxy
import sregraph.model

from sregraph.views import SharedParams


@SharedParams.getBottle.get('/dept')
def get_dept():
    print('test')
    pass

