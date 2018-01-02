#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/12/28 15:07
# @Author  : GanZiB
# @Email   : ganzib4fun@163.com
# @Site    : 
# @File    : config.py
# @Software: PyCharm
from consts import DB_URI

DEBUG = True
SQLALCHEMY_DATABASE_URI = DB_URI
SQLALCHEMY_TRACK_MODIFICATIONS = False
# session必须要设置key
SECRET_KEY = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
