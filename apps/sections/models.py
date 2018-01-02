#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/1/2 16:52
# @Author  : GanZiB
# @Email   : ganzib4fun@163.com
# @Site    : 
# @File    : models.py
# @Software: PyCharm
from flask_sqlalchemy import BaseQuery
from apps import db


class SectionsQuery(BaseQuery):
    def getall(self):
        return self.all()

    def getcategory_id(self, id):
        return self.get(id)


class Sections(db.Model):
    __tablename__ = 'sections'
    query_class = SectionsQuery
    book_id = db.Column(db.Integer, db.Sequence('book_id'), autoincrement=True)
    title = db.Column(db.String(255))
    content = db.Column(db.String(255))
    section_order = db.Column(db.Integer())
    section_url = db.Column(db.String(255), primary_key=True)
    book_name = db.Column(db.String(255))
    path = db.Column(db.String(255))

    def __init__(self, *args, **kwargs):
        super(Sections, self).__init__(*args, **kwargs)

    def __repr__(self):
        return '<user name %r>' % self.name