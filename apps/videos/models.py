# _*_ coding: utf-8 _*_
# @Time    : 2018/1/7 1:59
# @Author  : GanZiB
# @Site    : 
# @File    : models.py
# @Software: PyCharm
# @Email   : ganzib4fun@gmail.com
from flask_sqlalchemy import BaseQuery

from apps import db


class VideoQuery(BaseQuery):
    def getall(self):
        return self.all()

    def getcategory_id(self, id):
        return self.get(id)


class Video(db.Model):
    __tablename__ = 'videos'
    query_class = VideoQuery
    video_cd = db.Column(db.String(255), primary_key=True)
    video_url = db.Column(db.String(255))
    video_name = db.Column(db.String(255))
    video_author = db.Column(db.String(255))
    home_url = db.Column(db.String(255))
    cover = db.Column(db.String(255))
    author_cd = db.Column(db.String(255))
    spider_time = db.Column(db.metadata)


def __init__(self, *args, **kwargs):
    super(Video, self).__init__(*args, **kwargs)


def __repr__(self):
    return '<video name %r>' % self.video_name
