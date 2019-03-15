import re2

#detects hash dump
def hash_dump_pattern(str):
	for string in str.split("\n"):
		#/etc/passwd file entries for linux/mac 
		res1 = re2.search(r'^(\w+\:\S+\:\S*\d+\:\S*\d+\:.*\:\/\S+\:\/\S+)$',string)
		if not res1:
		#/etc/shadow file entries for linux  
			res2 = re2.search(r'^(\S+\:\$\d+\$\S+\$\S+\:\d+\:\d+\:\d+\:\d+)',string)
			if not res2:
		#password hashes for mac
				res3 = string.find("\"_writers_passwd\" => \\[")
				if res3 == -1:
		#Windwows NTLM dump 
					res4 = re2.search(r'^(\S+\:\d+\:[a-zA-Z0-9]{32}\:[a-zA-Z0-9]{32}\:)',string)
					if not res4:
		#windows Net-NTLM dump 
						res5=re2.search(r'^(\S+\:\:\w+\:[a-f0-9]{16}\:[a-f0-9]{32}\:[a-f0-9]{106})$',string)
						if not res5:
							return False
						else:
							return "Windows NTHash Dump Detected: "
					else:
						return "Windows Hash Dump Detected: "

				else:
					return "Mac Hash Dump Detected: "

			else:
				return "Linux Hash Dump Detected: "

		else:
			return "Dump Detected: /etc/passwd: "