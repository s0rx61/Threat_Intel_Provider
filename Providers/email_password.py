import re2

#detects emailaddresses/passwords
def email_password_pattern(str):
	count = 0
	res = re2.findall(r'(\w+\@\w+\.\w+)\:([\w!@#\$%\^&\*]{5,32})',str)
	if res:
		#detects unencrypted passwords
		for r in res:
			potential = r[1]
			if potential == "":
				break
			if not (len(potential)>5 and len(potential)<15):
				break
			if re2.search(r'\d',potential):
				count = count+1
			if re2.search(r'[A-Z]', potential):
				count = count+1
			if re2.search(r'[a-z]', potential):
				count = count+1
			if re2.search(r'[^a-z|A-Z|\s|0-9]',potential):
				count = count+1
			if count > 2:
				#return "Unencrypted Passwords Detected: "+':'.join(res[0])+"\n"
				return True
		#detects password hashes
		for r in res:
			str = r[1]
			res = re2.search(r'[a-f0-9]{32}',str)
			if res:
				#return "Password Hashes Detected: "+':'.join(res[0])+"\n"
				return True
	elif len(res) > 1:
		return "Emails Detected: "+':'.join(res[0])+"\n"
	return False