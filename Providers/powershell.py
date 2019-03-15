import re2

#detects powershell scripts
def powershell_pattern(str):
	ps = ["Add-Type","Start-Job","Get-Credential","Test-Connection","New-PSSession","Get-ADUser","Get-ADComputer",
	"Get-History","New-ISESnippet","Get-WMIObject","Get-CimInstance","Set-Location","Get-Content","Add-Content",
	"Set-Content","Copy-Item","Remove-Item","Move-Item","Set-Item","New-Item","Export-CliXML","Import-CliXML",
	"ConvertTo-XML","ConvertTo-HTML","Export-CSV","Import-CSV","ConvertTo-CSV","ConvertFrom-CSV","-ExecutionPolicy","New-Object"]

	for p in ps:
		if re2.search(p,str,re2.IGNORECASE):
			return "Powershell Script Detected: "