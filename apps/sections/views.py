#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/1/2 18:04
# @Author  : GanZiB
# @Email   : ganzib4fun@163.com
# @Site    : 
# @File    : views.py
# @Software: PyCharm
from flask import Blueprint, request, render_template, redirect, flash, session
from sqlalchemy import text

from apps.book.models import Book
from consts import session as sn

section = Blueprint('section', __name__, url_prefix='/section')
