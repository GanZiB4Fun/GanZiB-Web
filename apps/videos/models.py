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
	video_cd = db.Column(db.Integer, primary_key=True)
	video_url = db.Column(db.String(255))
	title = db.Column(db.String(255))
	tags = db.Column(db.String(255))
	keywords = db.Column(db.String(255))
	image_urls = db.Column(db.String(255))
	source = db.Column(db.String(255))
	category = db.Column(db.String(255))
	author = db.Column(db.String(255))
	head_img = db.Column(db.String(255))
	publish_date = db.Column(db.String(255))


def __init__(self, *args, **kwargs):
	super(Video, self).__init__(*args, **kwargs)


def __repr__(self):
	return '<video name %r>' % self.title
