import re2
import magic

#detects program code, executables and other formats
def code_pattern(str):
	with magic.Magic() as m:
		res = m.id_buffer(str)
	pattern = ["program","script","executable","source","shell","core","batch","bitmap"]
	if not(re2.match(r'^ASCII text*',res) or re2.match(r'^UTF-8 Unicode*',res)):
		for p in pattern:
			if p in res:
				return res