#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/1/2 18:04
# @Author  : GanZiB
# @Email   : ganzib4fun@163.com
# @Site    : 
# @File    : views.py
# @Software: PyCharm
import os

from flask import Blueprint, render_template
from sqlalchemy import text

from apps.sections.models import Sections
from consts import session as sn

section = Blueprint('section', __name__, url_prefix='/section')


@section.route('/<int:book_id>/<int:section_order>')
def get_content(book_id, section_order):
    if book_id and section_order:
        section_max = sn.query(Sections.section_order).filter(text('book_id=:book_id')).params(book_id=book_id).count()
        result_section = sn.query(Sections).filter(text('book_id=:book_id and section_order=:section_order')).params(
            book_id=book_id, section_order=section_order).first()
        path = result_section.path
        if section_order > 1:
            previous_order = section_order - 1
            previous_section = "/section/" + str(book_id) + "/" + str(previous_order)
        else:
            previous_section = None

        if (section_order + 1) <= section_max:
            next_order = section_order + 1
            next_section = "/section/" + str(book_id) + "/" + str(next_order)
        else:
            next_section = None

        if os.path.exists(path):
            title = result_section.title
            content = ''
            with open(path, 'r', encoding='utf-8') as fp:
                for line in fp:
                    content = content + line.replace("\n", '<br/>')
                fp.close()
                return render_template('section_info.html', title=title, content=content, next_section=next_section,
                                       previous_section=previous_section)
        else:
            return render_template('404.html')
    else:
        return render_template('404.html')
