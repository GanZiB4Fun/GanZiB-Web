#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/1/2 14:24
# @Author  : GanZiB
# @Email   : ganzib4fun@163.com
# @Site    : 
# @File    : models.py
# @Software: PyCharm
from flask_sqlalchemy import BaseQuery
from apps import db


class CategoryQuery(BaseQuery):
    def getall(self):
        return self.all()

    def getcategory_id(self, id):
        return self.get(id)


class Category(db.Model):
    __tablename__ = 'categorys'
    query_class = CategoryQuery
    category_id = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.String(200), unique=True)

    def __init__(self, *args, **kwargs):
        super(Category, self).__init__(*args, **kwargs)

    def __repr__(self):
        return '<category name %r>' % self.category_name
