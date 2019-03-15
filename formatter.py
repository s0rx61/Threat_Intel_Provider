
#Title: formatter
#formats data into json

headers_data = ['KEY', 'NAME', 'PASTE_TIMESTAMP', 'DOWNLOAD_TIMESTAMP', 'SHA256',
'MD5', 'FUZZYHASH', 'RAWDATA']
headers_ip = ['KEY', 'NAME', 'PASTE_TIMESTAMP', 'DOWNLOAD_TIMESTAMP', 'IP']
headers_execs = ['KEY', 'NAME', 'PASTE_TIMESTAMP','DOWNLOAD_TIMESTAMP','SHA256',
'MD5', 'FUZZYHASH', 'RAWDATA', 'CLAMAV']
headers_hashdump = ['KEY', 'NAME', 'PASTE_TIMESTAMP', 'DOWNLOAD_TIMESTAMP', 'SHA256',
'MD5', 'FUZZYHASH', 'RAWDATA']
headers_creds = ['KEY', 'NAME', 'PASTE_TIMESTAMP', 'DOWNLOAD_TIMESTAMP', 'SHA256',
'MD5', 'FUZZYHASH', 'RAWDATA', 'TYPE']
headers_domains = ['KEY', 'NAME', 'PASTE_TIMESTAMP', 'DOWNLOAD_TIMESTAMP', 'SHA256',
'MD5', 'FUZZYHASH', 'RAWDATA']
headers_base64 = ['KEY', 'NAME', 'PASTE_TIMESTAMP', 'DOWNLOAD_TIMESTAMP', 'SHA256',
'MD5', 'FUZZYHASH', 'RAWDATA', 'TYPE', 'CLAMAV']
headers_powershell = ['KEY', 'NAME', 'PASTE_TIMESTAMP', 'DOWNLOAD_TIMESTAMP', 'SHA256',
'MD5', 'FUZZYHASH', 'RAWDATA']

def format_json(result, table):
	json_result = "{ 'records' : [\n{\n"
	i = 0
	if table == "data":
		header = headers_data
	elif table == "ip":
		header = headers_ip
	elif table == "execs":
		header = headers_execs
	elif table == "hashdump":
		header = headers_hashdump
	elif table == "creds":
		header = headers_creds
	elif table == "domains":
		header = headers_domains
	elif table == "base64":
		header = headers_base64
	elif table == "powershell":
		header = headers_powershell

	length = len(header)

	for r in result:
		for i in range(0, length-1):
			json_result = json_result + "'" + header[i] + "'" + ":" + "'" + r[i]  + "'" + ",\n"
		json_result = json_result[:-1] + "\n},"

	json_result = json_result[:-1] + "]}"

	return json_result



