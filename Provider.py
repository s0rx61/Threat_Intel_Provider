
#Title: Provider
#Runs all the providers for the given list of parameters and inserts the results into appropriate DB tables

import Providers.base64
import Providers.email_password
import Providers.hash_dump
import Providers.ipaddress
import Providers.keys
import Providers.powershell
import Providers.source_code
import CSPDatabase

def analyze(list):
	connection,cursor = CSPDatabase.get_connection()
	rawdata = list[7]
	list = list[:-1]

	result = Providers.base64.base64_pattern(rawdata)
	if result != None:
		list_base64 = list
		list_base64.append(result)
		#CLAMAV integreation
		clamav_id = "null"
		list_base64 = list_base64.append(clamav_id)
		print list_base64
		CSPDatabase.insert_table(connection,cursor,"base64",list.append(clamav_id))

	result = Providers.email_password.email_password_pattern(rawdata)
	if result != False:
		list_email_password = list
		list_email_password.append(result)
		list_email_password.append("Email-Passwords")
		CSPDatabase.insert_table(connection,cursor,"creds",list_email_password)

	result = Providers.hash_dump.hash_dump_pattern(rawdata)
	if result != False and "with no line terminators" not in result:
		list_hash_dump = list
		list_hash_dump = list_hash_dump.append(result)

		CSPDatabase.insert_table(connection,cursor,"hashdump",list_hash_dump)


	result = Providers.keys.key_pattern(rawdata)
	if result != False:
		list_keys = list
		list_keys.append(result)
		list_keys.append("Keys")
		CSPDatabase.insert_table(connection,cursor,"creds",list_keys)

	result = Providers.powershell.powershell_pattern(rawdata)
	if result == True:
		list_powershell = list
		#CLAMAV integreation
		clamav_id = "null"
		list_powershell.append(clamav_id)
		
		CSPDatabase.insert_table(connection,cursor,"powershell",list_powershell)


	result = Providers.source_code.code_pattern(rawdata)
	if result != None:
		list_source_code = list
		list_source_code.append(result)
		#CLAMAV integreation
		clamav_id = "null"
		list_source_code.append(clamav_id)
		CSPDatabase.insert_table(connection,cursor,"execs",list_source_code)


