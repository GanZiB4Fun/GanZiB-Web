#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/1/2 16:17
# @Author  : GanZiB
# @Email   : ganzib4fun@163.com
# @Site    : 
# @File    : models.py
# @Software: PyCharm
from flask_sqlalchemy import BaseQuery
from apps import db


class BookQuery(BaseQuery):
    def getall(self):
        return self.all()

    def getcategory_id(self, id):
        return self.get(id)


class Book(db.Model):
    __tablename__ = 'books'
    query_class = BookQuery
    book_id = db.Column(db.Integer, db.Sequence('book_id'), autoincrement=True)
    book_name = db.Column(db.String(255))
    author = db.Column(db.String(255))
    category = db.Column(db.String(255))
    start_url = db.Column(db.String(255), primary_key=True)
    catch_date = db.Column(db.String(255))
    status = db.Column(db.String(255))

    def __init__(self, *args, **kwargs):
        super(Book, self).__init__(*args, **kwargs)

    def __repr__(self):
        return '<user name %r>' % self.name
