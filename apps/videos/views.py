# _*_ coding: utf-8 _*_
# @Time    : 2018/1/7 2:04
# @Author  : GanZiB
# @Site    : 
# @File    : views.py
# @Software: PyCharm
# @Email   : ganzib4fun@gmail.com
from flask import Blueprint, render_template
from sqlalchemy import text

from apps.videos.models import Video
from consts import session as sn

video = Blueprint('video', __name__, url_prefix='/video')


@video.route('/list/page/<int:page_num>')
def get_video_list(page_num=1):
	title = '视频'
	pagination = Video.query.paginate(page=page_num, per_page=10)
	return render_template('video/video_list.html', pagination=pagination, title=title, )


@video.route('/<string:video_cd>')
def get_video_info(video_cd):
	video_info = sn.query(Video).filter(text('video_cd=:video_cd')).params(video_cd=video_cd).first()
	content = '<video src="' + video_info.video_url + '" volume="0.5" poster="' + video_info.image_urls + '" controls="" preload="true" playsinline="" webkit-playsinline="webkit-playsinline" x-webkit-airplay="allow"  style="transform-origin: 0px 0px 0px; opacity: 1; transform: scale(1, 1);"></video>'
	return render_template('video/video_info.html', content=content, video=video_info)
