import re2

#detects private IP address
def ipaddress_pattern(str):
	ip_list = set()
	res = re2.findall(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}',str)
	for r in res:
		if not (re2.match(r'(^127\.)|(^10\.)|(^172\.1[6-9]\.)|(^172\.2[0-9]\.)|(^172\.3[0-1]\.)|(^192\.168\.)',r)):
			ip_list.add(r)
	if ip_list:
		return ip_list