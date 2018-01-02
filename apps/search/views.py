# _*_ coding: utf-8 _*_
# @Time    : 2018/1/3 0:42
# @Author  : GanZiB
# @Site    : 
# @File    : views.py
# @Software: PyCharm
# @Email   : ganzib4fun@gmail.com
from flask import Blueprint, request, render_template, redirect, flash, session
from sqlalchemy import text

from apps.book.models import Book
from apps.sections.models import Sections
from consts import session as sn

search = Blueprint('search', __name__, url_prefix='/search')


@search.route('/book', methods=['POST'])
def get_book_by_id():
	book_name = request.form['book_name']
	result_book = sn.query(Book).filter(text('book_name=:book_name')).params(book_name=book_name).first()
	sections = sn.query(Sections).filter(text('book_id=:book_id')).params(book_id=result_book.book_id).order_by(
		'section_order').all()
	return render_template('book_catalog.html', book=result_book, sections=sections, title=result_book.book_name)
