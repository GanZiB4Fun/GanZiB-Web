#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/1/11 11:11
# @Author  : GanZiB
# @Email   : ganzib4fun@163.com
# @Site    : 
# @File    : views.py
# @Software: PyCharm
from flask import Blueprint, render_template

alipay = Blueprint('alipay', __name__, url_prefix='/alipay')


@alipay.route('/')
def get_hongbao():
    return render_template('alipay.html')
