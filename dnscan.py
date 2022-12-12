"""
File:        dnscan.py
Description: Subdomain enumeration program in reconnaissance for web pentest.
"""

import requests 
import sys 

# open txt file and real all content
subdomain_list = open("subdomains1000.txt").read()
# split by new lines
subdomains = subdomain_list.splitlines()

for subdomain in subdomains:
    # construct the urs with domain supplied in the command line
    url = f"http://{subdomain}.{sys.argv[1]}" 
    # send request, no response means subdomain doesn't exist
    try:
        requests.get(url)
    
    except requests.ConnectionError: 
        # print nothing and pass if no subdomain exist
        pass
    
    else:
        print("[+] Discovered Subdomain: ",url)
