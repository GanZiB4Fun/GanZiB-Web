#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/1/15 17:42
# @Author  : GanZiB
# @Email   : ganzib4fun@163.com
# @Site    : 
# @File    : weixinlogin.py
# @Software: PyCharm
import hashlib

from flask import Blueprint, render_template, request

weixin = Blueprint('weixin', __name__, url_prefix='/weixin')


@weixin.route('/login')
def wechat_login():
    return render_template('weixin/wechat_login.html')


@weixin.route('/login2')
def wechat_login2():
    code = request.form['code']
    url = "https://api.weixin.qq.com/sns/oauth2/access_token?appid=APPID&secret=SECRET&code=CODE&grant_type=authorization_code"
    return render_template('')


@weixin.route('/wechat', methods=['GET', 'POST'])
def wechat():
    if request.method == 'GET':
        # 这里改写你在微信公众平台里输入的token
        token = 'weixin'
        # 获取输入参数
        data = request.args
        signature = data.get('signature', '')
        timestamp = data.get('timestamp', '')
        nonce = data.get('nonce', '')
        echostr = data.get('echostr', '')
        # 字典排序
        list = [token, timestamp, nonce]
        list.sort()

        s = list[0] + list[1] + list[2]
        # sha1加密算法
        hascode = hashlib.sha1(s.encode('utf-8')).hexdigest()
        # 如果是来自微信的请求，则回复echostr
        if hascode == signature:
            return echostr
        else:
            return ""
