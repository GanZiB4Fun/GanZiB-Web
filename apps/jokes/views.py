#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/1/5 14:01
# @Author  : GanZiB
# @Email   : ganzib4fun@163.com
# @Site    : 
# @File    : views.py
# @Software: PyCharm
from flask import Blueprint, render_template

from apps.jokes.models import Joke

joke = Blueprint('joke', __name__, url_prefix='/joke')


@joke.route('/list/page/<int:page_num>')
def get_joke_list(page_num=1):
    title = '内涵段子'
    pagination = Joke.query.paginate(page=page_num, per_page=10)
    return render_template('joke/joke_list.html', pagination=pagination, title=title, )
