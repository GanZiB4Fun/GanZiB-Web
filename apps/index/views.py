#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/1/2 14:23
# @Author  : GanZiB
# @Email   : ganzib4fun@163.com
# @Site    : 
# @File    : views.py
# @Software: PyCharm

from flask import Blueprint, render_template

from apps.category.models import Category

index = Blueprint('index', __name__)


@index.route('/')
@index.route('page/<int:pageid>')
def index_1(pageid=1):
    categorys = Category.query.getall()
    return render_template('index.html',
                           categorys=categorys, nav_current="index")
