#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/1/2 13:06
# @Author  : GanZiB
# @Email   : ganzib4fun@163.com
# @Site    : 
# @File    : __init__.py.py
# @Software: PyCharm
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)
