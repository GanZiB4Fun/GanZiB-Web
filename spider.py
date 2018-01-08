#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/1/5 17:18
# @Author  : GanZiB
# @Email   : ganzib4fun@163.com
# @Site    : 
# @File    : spider.py
# @Software: PyCharm
import hashlib
import json
import time
import urllib.error
import urllib.request

import pymysql

conn = pymysql.connect(host='127.0.0.1',
					   port=3306,
					   user='root',
					   password='root',
					   db='r',
					   charset='utf8')


def str_encrypt(str):
	"""
	使用sha1加密算法，返回str加密后的字符串
	"""
	try:
		sha = hashlib.sha1(str.encode('utf-8'))
		encrypts = sha.hexdigest()
		return encrypts
	except BaseException as e:
		print(str)
		print(e)
		return None


def catch_video(url):
	resp = ''
	try:
		resp = urllib.request.urlopen(url=url, timeout=30).read()
	except urllib.error as e:
		return
	json_str = resp.decode('utf-8')
	json_data = json.loads(json_str)
	video_list = json_data.get('result')
	for video in video_list:
		video_url = video.get('video_url')
		if video_url:
			video_cd = str_encrypt(video_url)
			title = video.get('title')
			tags = str(video.get('tags'))
			keywords = str(video.get('keywords'))
			image_urls = video.get('image_urls')
			image_url = ''
			if len(image_urls) > 0:
				image_url = image_urls[0]
			source = video.get('source')
			category = video.get('category')
			author = video.get('wemedia_info').get('name')
			head_img = video.get('wemedia_info').get('image')
			publish_date_str = video.get('date')
			try:
				cur = conn.cursor()
				cur.execute(
					"INSERT INTO videos (video_cd,video_url,title,tags,keywords,image_urls,source,category,author,head_img,publish_date) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
					(video_cd, video_url, title, tags, keywords, image_url, source, category, author, head_img,
					 publish_date_str))
				conn.commit()
				print('成功采集视频---' + title)
			except BaseException as e:
				print(e)
				pass


def start():
	index = 1
	url_tamp = 'http://www.yidianzixun.com/home/q/news_list_for_channel?channel_id=u13746&cstart=CSTART_NUM&cend=CEND_NUM&infinite=true&refresh=1&__from__=pc&multi=5&appid=web_yidian&_='
	while True:
		millis = int(round(time.time() * 1000))
		url = url_tamp + str(millis)
		url = url.replace('CSTART_NUM', str(index * 10))
		url = url.replace('CEND_NUM', str((index + 1) * 10))
		catch_video(url)
		time.sleep(10)
		if index * 10 >= 50:
			index = 1
			millis = int(round(time.time() * 1000))
			time.sleep(20)
		index = index + 1


if __name__ == '__main__':
	start()
