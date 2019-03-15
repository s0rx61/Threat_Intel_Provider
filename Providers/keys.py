
#Title: keys
#Regex to detect google key, aws access key, aws client id, heroku api key and private key


import re2
import Providers.entropy

#detects API keys, privates keys
def key_pattern(str):	
	pattern_list = [(r'^[a-zA-Z0-9_]{39}$','google_key'),
  #('^[0-9a-z]{40}$','git_oauth'),
  (r'^(?<![A-Za-z0-9/+=])[A-Za-z0-9/+=]{40}(?![A-Za-z0-9/+=])$','aws_access_key'),
  (r'^AKIA[0-9A-Z]{16}$','aws_client_id'),
  (r'^[0-9A-F]{8}-[0-9A-F]{4}-[0-9A-F]{4}-[0-9A-F]{4}-[0-9A-F]{12}$','heroku_api')]

	check1=re2.search(r'\s+',str) # eliminate files with no whitespaces
	 
	for string in re2.split(r'\s+',str):
		for pattern in pattern_list:
			if check1 != None:
				res1 = re2.search(pattern[0],string) # checks for key pattern 
				res2 = len(re2.findall(r'[0-9]',string)) # eliminates strings with no digits
				res3 = re2.search('http',string) # eliminates hyperlinks
				res4 = re2.match(r'[A-Z]',string) # eliminates strings with no uppercase letters
				if res1 and res2>1 and not res3 and Providers.entropy.entropy(string)>20 and res4!=None:
					print string
					return "Key Detected: "+pattern[1]+" :"+res1.group()+" :"

		if (string.find("-----BEGIN") is not -1 and string.find("PRIVATE KEY-----") is not -1):
			return "Private Key Detected: "	
	return False