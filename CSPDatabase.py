
#Title: ProviderDatabase
#Creates database connections. Inserts and retreives data from database

import psycopg2
from psycopg2 import Error

import formatter

def get_connection():
	try:
		connection = psycopg2.connect(user = "", password = "", host = "", port = "", database = "")
		cursor = connection.cursor()
		return connection, cursor
	except (Exception, psycopg2.DatabaseError) as error:
		print ("Error while creating PostgreSQL table", error)

#def create_table():
def insert_table(connection, cursor, table_name, list):
	try:
		if table_name == "data" :
			cursor.execute("INSERT INTO data (KEY, NAME, PASTE_TIMESTAMP, DOWNLOAD_TIMESTAMP, SHA256, MD5, FUZZYHASH, RAWDATA) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)", (list[0], list[1], list[2], list[3], list[4], list[5], list[6], list[7]))		
		elif table_name == "ip" :
			cursor.execute("INSERT INTO ip (KEY, NAME, PASTE_TIMESTAMP, DOWNLOAD_TIMESTAMP, IP) VALUES (%s, %s, %s, %s, %s, %s)", (list[0], list[1], list[2], list[3], list[4], list[5]))
		elif table_name == "execs" :
			cursor.execute("INSERT INTO execs (KEY, NAME, PASTE_TIMESTAMP, DOWNLOAD_TIMESTAMP, SHA256, MD5, FUZZYHASH, RAWDATA, TYPE, CLAM_AV) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (list[0], list[1], list[2], list[3], list[4], list[5], list[6], list[7], list[8], list[9]))
		elif table_name == "hashdump" :
			cursor.execute("INSERT INTO hashdump (KEY, NAME, PASTE_TIMESTAMP, DOWNLOAD_TIMESTAMP, SHA256, MD5, FUZZYHASH, RAWDATA) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)", (list[0], list[1], list[2], list[3], list[4], list[5], list[6], list[7]))
		elif table_name == "creds" :
			cursor.execute("INSERT INTO creds (KEY, NAME, PASTE_TIMESTAMP, DOWNLOAD_TIMESTAMP, SHA256, MD5, FUZZYHASH, RAWDATA, TYPE) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)", (list[0], list[1], list[2], list[3], list[4], list[5], list[6], list[7], list[8]))
		elif table_name == "domains" :
			cursor.execute("INSERT INTO domains (KEY, NAME, PASTE_TIMESTAMP, DOWNLOAD_TIMESTAMP, SHA256, MD5, FUZZYHASH, RAWDATA) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)", (list[0], list[1], list[2], list[3], list[4], list[5], list[6], list[7]))
		elif table_name == "base64" :
			cursor.execute("INSERT INTO base64 (KEY, NAME, PASTE_TIMESTAMP, DOWNLOAD_TIMESTAMP, SHA256, MD5, FUZZYHASH, RAWDATA, TYPE, CLAM_AV) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (list[0], list[1], list[2], list[3], list[4], list[5], list[6], list[7], list[8], list[9]))
		elif table_name == "powershell" :
			cursor.execute("INSERT INTO powershell (KEY, NAME, PASTE_TIMESTAMP, DOWNLOAD_TIMESTAMP, SHA256, MD5, FUZZYHASH, RAWDATA, CLAM_AV) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)", (list[0], list[1], list[2], list[3], list[4], list[5], list[6], list[7], list[8]))

		connection.commit() 
		print "Records inserted successfully "+table_name

	except (Exception, psycopg2.DatabaseError) as error:
		if(connection):
			connection.rollback()
			if "duplicate" not in str(error):
				print("Failed inserting record into table {}: {:s}".format(error, table_name))
				print list

#select data from a table
def select_table_by_number( connection, cursor, table, number=20):
	try:
		query = "SELECT * from {:s} ORDER BY DOWNLOAD_TIMESTAMP DESC LIMIT {:d}".format(table, number) 
		cursor.execute(query)
		result = cursor.fetchall()
		return formatter.format_json(result, table)

	except (Exception, psycopg2.DatabaseError) as error:
		if(connection):
			connection.rollback()
		return "error"

def select_table_by_id( connection, cursor, table, id):
	try:
		query = "SELECT * from {:s} WHERE KEY = '{:s}'".format(table, id) 
		cursor.execute(query)
		result = cursor.fetchall()
		return formatter.format_json(result, table)

	except (Exception, psycopg2.DatabaseError) as error:
		if(connection):
			connection.rollback()
		return "error"

def select_table_by_hash( connection, cursor, type, hash, table="data"):
	try:
		query = "SELECT * from data WHERE {:s} = '{:s}'".format(table, type, hash) 
		cursor.execute(query)
		result = cursor.fetchall()
		return formatter.format_json(result, table)

	except (Exception, psycopg2.DatabaseError) as error:
		if(connection):
			connection.rollback()
		return "error"

def select_all_table( connection, cursor, table):
	try:
		query = "SELECT * from {:s}".format(table) 
		cursor.execute(query)
		result = cursor.fetchall()
		return result

	except (Exception, psycopg2.DatabaseError) as error:
		if(connection):
			connection.rollback()
		return "error"

def select_table_by_salesforce( connection, cursor, limit):
	try:
		query = "SELECT * from data LIMIT {:s}".format(limit) 
		cursor.execute(query)
		result = cursor.fetchall()
		return result

	except (Exception, psycopg2.DatabaseError) as error:
		if(connection):
			connection.rollback()
		return "error"

def select_table_by_date( connection, cursor, table, date):
	date = date.replace("-", "/")
	try:
		query = "SELECT * from {:s} WHERE DOWNLOAD_TIMESTAMP LIKE '{:s}%'".format(table, date)
		cursor.execute(query)
		result = cursor.fetchall()
		return formatter.format_json(result, table)

	except (Exception, psycopg2.DatabaseError) as error:
		if(connection):
			connection.rollback()
		return "error"