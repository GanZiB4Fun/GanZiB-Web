#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/1/2 15:03
# @Author  : GanZiB
# @Email   : ganzib4fun@163.com
# @Site    : 
# @File    : views.py
# @Software: PyCharm
from flask import Blueprint, request, render_template, redirect, flash, session
from sqlalchemy import text

from apps.user.models import User
from consts import session as sn

user = Blueprint('user', __name__, url_prefix='/user')


@user.route('/login', methods=['GET', 'POST'])
def user_login():
    if request.method == 'GET':
        return render_template('login2.html')
    else:
        username = request.form['name']
        passwords = request.form['pwd']
        user = sn.query(User).filter(text('name=:name and passwords=:passwords')).params(name=username,
                                                                                         passwords=passwords).first()
        if user:
            session['logged_in'] = True
            session['user_id'] = user.id
            session['username'] = user.name
            return redirect('/', code=302)
        else:
            return render_template('404.html')


@user.route('/register', methods=['GET', 'POST'])
def user_register():
    if request.method == 'GET':
        return render_template('register2.html')
    elif request.method == 'POST':
        username = request.form['name']
        password = request.form['pwd']
        email = request.form['email']
        user = User(username, password, email)
        sn.add(user)
        sn.commit()
        return redirect('/')


@user.route('/logout', methods=['GET'])
def user_logout():
    session.pop('logged_in', None)
    flash('You were logged out')
    return redirect('/')
