#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/1/5 13:57
# @Author  : GanZiB
# @Email   : ganzib4fun@163.com
# @Site    : 
# @File    : models.py
# @Software: PyCharm
from flask_sqlalchemy import BaseQuery

from apps import db


class JokeQuery(BaseQuery):
    def getall(self):
        return self.all()

    def getcategory_id(self, id):
        return self.get(id)


class Joke(db.Model):
    __tablename__ = 'jokes'
    query_class = JokeQuery
    joke_cd = db.Column(db.Integer, primary_key=True, autoincrement=True)
    joke_url = db.Column(db.String(255))
    content = db.Column(db.String(255))
    like_num = db.Column(db.Integer)
    diss_num = db.Column(db.Integer)
    author = db.Column(db.String(255))
    head_img = db.Column(db.String(255))
    star_num = db.Column(db.Integer)
    spider_date = db.Column(db.metadata)

    def __init__(self, *args, **kwargs):
        super(Joke, self).__init__(*args, **kwargs)

    def __repr__(self):
        return '<joke name %r>' % self.content
