#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/1/2 16:10
# @Author  : GanZiB
# @Email   : ganzib4fun@163.com
# @Site    : 
# @File    : views.py
# @Software: PyCharm
from flask import Blueprint, request, render_template, redirect, flash, session
from sqlalchemy import text

from apps.book.models import Book
from apps.category.models import Category
from consts import session as sn

category = Blueprint('category', __name__, url_prefix='/category')


@category.route('/<int:category_id>')
def get_books_by_category_id(category_id=1):
    category_entry = sn.query(Category).filter(text('category_id=:category_id')).params(category_id=category_id).first()
    category_name = category_entry.category
    books = sn.query(Book).filter(text('category=:category')).params(category=category_name).all()
    return render_template('books_list.html', title=category_name + '--小说列表', books=books)
