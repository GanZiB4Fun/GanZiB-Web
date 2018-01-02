#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/1/2 16:45
# @Author  : GanZiB
# @Email   : ganzib4fun@163.com
# @Site    : 
# @File    : views.py
# @Software: PyCharm
from flask import Blueprint, request, render_template, redirect, flash, session
from sqlalchemy import text

from apps.book.models import Book
from consts import session as sn

book = Blueprint('book', __name__, url_prefix='/book')


@book.route('<int:book_id>')
def get_book_by_id(book_id):
    result_book = sn.query(Book).filter(text('book_id=:book_id')).params(book_id=book_id).first()
    return render_template('book_catalog.html')
