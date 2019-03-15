# Provider Tool

Websites like pastebin are popular websites for storing and sharing text. Though they are mostly used for distributing legitimate data, they are frequently used as a public repository of stolen information, such as network configuration details, authentication records, domain/entry point enumeration, malware hosting, etc.

The purpose of this project is to develop a system that periodically pulls the data from these sites and analyze the data to find indicators.  

# ProviderScraper
Scraper is used to pull enries periodically and store them in the database. Currently only pastebin.com is supported.

# ProviderAnalyzer
Analyzer performs following tasks
1. Identify API, keys dumped post exploitation
2. Domain dumps for facilitating further attacks
4. Email Addresses dumps
5. Password dumps
6. Hash dumps for windows, mac, linux
7. Source code and executable 
8. Extract IP addresses
9. base64 encoded data
10. PowerShell scripts 
11. Extract hyperlinks

Functionality includes API capability for future integrations



