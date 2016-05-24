# coding=utf-8
import requests
import json
import time


file = open("adr")
while True:
	line = file.readline()
	if not line: break
	# Get the feed
	r = requests.get("http://zip5.5432.tw/zip5json.py?adrs="+line)
	r.text

	# Convert it to a Python dictionary
	data = json.loads(r.text)
	print (data['new_adrs'])
	time.sleep(0.5)
