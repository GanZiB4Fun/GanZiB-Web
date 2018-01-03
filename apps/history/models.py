#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/1/3 18:39
# @Author  : GanZiB
# @Email   : ganzib4fun@163.com
# @Site    : 
# @File    : models.py
# @Software: PyCharm
from flask_sqlalchemy import BaseQuery

from apps import db


class HistoryQuery(BaseQuery):
    def getall(self):
        return self.all()

    def getcategory_id(self, id):
        return self.get(id)


class History(db.Model):
    __tablename__ = 'read_history'
    query_class = HistoryQuery
    history_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    book_id = db.Column(db.Integer)
    user_id = db.Column(db.Integer)
    section_id = db.Column(db.Integer)

    def __init__(self, book_id, user_id, section_id):
        self.book_id = book_id
        self.user_id = user_id
        self.section_id = section_id

    def __repr__(self):
        return '<History name %r>' % self.history_id
