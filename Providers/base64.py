import re2

#detects base64 encoded files
def base64_pattern(str):
	b64 = [(r'\bTV(oA|pB|pQ|qA|qQ|ro)',"b64_exe"),
	(r'^f0VM',"b64_elf"),
	(r'^UEs',"b64_zip"),
	(r'^UmFy',"b64_rar"),
	(r'^H4sI',"b64_gzip"),
	(r'aHR0cDov|SFRUUDov|d3d3Lg|V1dXLg',"b64_url"),
	(r'^0M8R4',"b64_doc"),
	(r'^e1xydGY',"b64_rtf"),
	(r'^PD94bWwg',"b64_xml")]

	b64_docx = ["d29yZC9fcmVsc", # word/_rel
	"Zm9udFRhYmxl", # fontTable
	"ZG9jUHJvcHM", # docProps
	"Q29udGVudF9UeXBlcw", # Content_Types
	"c2V0dGluZ3M"] #settings

	b64_xml_doc = ["b3BlbmRvY3VtZW50", # opendocument
	"InBhcmFncmFwaCI", # "paragraph"
	"b2ZmaWNlL3dvcmQv", # office/word/
	"RG9jdW1lbnRQcm9wZXJ0aWVz"] # DocumentProperties

	for b in b64:
		if re2.match(b[0],str):
			if b[1] == "b64_xml":
				count=0
				for i in b64_xml_doc:
					if re2.match(i,str[3:]):
						count = count+1
				if count == 3:
					return "b64_xml_doc"
			elif b[1] == "b64_zip":
				count = 0
				for i in b64_docx:
					if re2.match(i,str[3:]):
						count = count+1
				if count == 3:
					return "b64_docx"
			else:
				return b[1]