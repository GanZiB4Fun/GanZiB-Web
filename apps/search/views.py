# _*_ coding: utf-8 _*_
# @Time    : 2018/1/3 0:42
# @Author  : GanZiB
# @Site    : 
# @File    : views.py
# @Software: PyCharm
# @Email   : ganzib4fun@gmail.com
from flask import Blueprint, request, render_template

from apps.book.models import Book
from consts import session as sn

search = Blueprint('search', __name__, url_prefix='/search')


@search.route('/book', methods=['POST'])
def get_book_by_id():
    book_name = request.form['book_name']
    result_book = sn.query(Book).filter(Book.book_name.like('%' + book_name + '%'))
    return render_template('xiaoshuo/book_catalog.html', books=result_book, title="搜索" + book_name,
                           search="“" + book_name + "” ")
