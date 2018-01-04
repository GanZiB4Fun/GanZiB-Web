#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/1/3 20:30
# @Author  : GanZiB
# @Email   : ganzib4fun@163.com
# @Site    : 
# @File    : views.py
# @Software: PyCharm
from flask import Blueprint, render_template
from sqlalchemy import text

from apps.history.models import History
from apps.sections.models import Sections
from consts import session as sn

history = Blueprint('history', __name__, url_prefix='/history')


@history.route('/list/<int:user_id>')
def get_history_list(user_id):
    history_list = sn.query(History).filter(text('user_id=:user_id')).params(user_id=user_id).all()
    section_list = []
    for i in history_list:
        section = sn.query(Sections).filter(text('book_id=:book_id and section_order=:section_order')).params(
            book_id=i.book_id, section_order=i.section_id).first()
        section_list.append(section)

    return render_template('history.html', sections=section_list, title='阅读历史')
