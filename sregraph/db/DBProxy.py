#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'Administrator'
__mtime__ = '2019/4/3 0003'
"""

from py2neo import Graph
from os import getenv


class DBProxy(object):
    '''
    Provide SigletonMode to get dbconnection
    '''
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls,'_instance'):
            org = super(DBProxy,cls)
            cls._instance = org.__new__(cls,*args,**kwargs)
        return cls._instance

    def getNeoConn(self):
        return Graph(password=getenv("NEO4J_PASSWORD"))
