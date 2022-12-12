# pythonProject
CIS1415 Intro to programming
program: 

<h3>Banner Grabbing (infoGrabber.py)</h3>
This is a simple program created in python that gives us banner info from GET requests, and provides server information.
<br>syntax:
py -3 infoGrabber.py "WEBSITE.COM"

<h3>Subdomain Enumeration (dnscan.py)</h3>
This program helps us brute forcing subdomain enumeration. It helps to broaden the attack surface and find hidden applications and forgotten subdomain.
<br>syntax:
py -3 dnscan.py <url>

<h3>Cracking Hashes (hashCrack.py)</h3>
This program helps us crack SHA1 passwords into plaintext using a dictionary wordlist file.
<br>syntax:  
hashcrack.py -sha1 [HASH] -w [dictionary.txt]
