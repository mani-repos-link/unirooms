#from flask import Flask, jsonify
import json
from datetime import date
import feedparser as fp

feed = fp.parse('http://aws.unibz.it/risweb/timetable.aspx?showtype=0&format=rss')


def get_today_date():
	return str(date.today().strftime('%d.%m.%Y'))

def get_entries():
	data = []
	for entry in feed.entries:
		entry = entry.summary
		print(entry)
		info = entry.split(' - ')
		m = {}
		m['date'] = info[0]
		m['time'] = info[1]
		m['title'] = info[2]
		m['room'] = info[3] if len(info)>4 else ''
		m['lecturer'] = info[4] if len(info)>4 else ''
		data.append(m)
	return data

if __name__ == '__main__':
	with open('somefile.json','w') as f:
		json.dump(get_entries(), f)
	#print(get_entries)