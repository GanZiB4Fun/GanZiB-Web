#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/1/2 14:57
# @Author  : GanZiB
# @Email   : ganzib4fun@163.com
# @Site    : 
# @File    : models.py
# @Software: PyCharm
from flask_sqlalchemy import BaseQuery
from apps import db


class UserQuery(BaseQuery):
    def getall(self):
        return self.all()

    def getcategory_id(self, id):
        return self.get(id)


class User(db.Model):
    __tablename__ = 'users'
    query_class = UserQuery
    id = db.Column(db.Integer, db.Sequence('id'), primary_key=True, autoincrement=True)
    name = db.Column(db.String(50))
    passwords = db.Column(db.String(50))
    email = db.Column(db.String(50))

    def __init__(self, name, passwords, email):
        self.name = name
        self.passwords = passwords
        self.email = email

    def __repr__(self):
        return '<user name %r>' % self.name
