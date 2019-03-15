
#Title: Provider
#Retreives data from pastebin periodically and inserts them into databse

import os
import requests
import json
import time
from datetime import datetime
import subprocess
import hashlib
import ssdeep

import ProviderDatabase 
import Providers.salesforce
import Provider

Limit = "250" #request 'x' lastest public entries
Frequency = 60 #run scraper every 'x' secs
history_size = 5000 #number of lines in download_history file


#get raw data given a pastebin id
def get_api_raw_data(pastebin_id):
	response  =  requests.get('https://scrape.pastebin.com/api_scrape_item.php?i='+pastebin_id)
	if response.status_code != 200:
		print "Request failed with code "+response.status_code+". Exiting..."
		return None
	return response.text

#get recent public entries using scraper API
def scraper(connection, cursor):
	url  =  "http://scrape.pastebin.com/api_scraping.php?limit = "+Limit
	response  =  requests.get(url)
	status_code = response.status_code
	if response.status_code != 200:
		print "Request failed with code "+response.status_code+". Exiting..."
		return
	list_new  =  json.loads(response.text)
	for item in list_new:
		scrape_url = item['scrape_url']
		title = (item['title'] if item['title'] != "u\'\'" else "null")
		key = item['key']
		syntax = item['syntax']
		size = item['size']
		date = item['date']
		user = item['user']
		raw_data = get_api_raw_data(key).encode("utf-8")
		sha256 = hashlib.sha256(raw_data).hexdigest()
		md5 = hashlib.md5(raw_data).hexdigest()
		fuzzyhash = ssdeep.hash(raw_data)
		time_now = str(datetime.strftime(datetime.utcnow(), '%Y/%m/%d/%H/%M/%S'))
		list = [key, title, date, time_now, sha256, md5, fuzzyhash, raw_data]
	
		#send data to DB
		ProviderDatabase.insert_table(connection, cursor, "data", list)

		#analyze the raw_data
		Provider.analyze(list)


def main():
	connection, cursor = ProviderDatabase.get_connection()
	while True:
		scraper(connection, cursor)
		time.sleep(Frequency)

	if(connection):
		cursor.close()
		connection.close()
		print("PostgreSQL connection is closed")

if __name__ == "__main__":
	main()
