"""
File:        infoGrabber.py
Description: This program helps users gather information from a webserver by
             sending a HTTP request. It can be run from the command line
             interface.

"""
# import necessry modules
import sys 
import requests
import socket
import json

# error message if url not provided
if len(sys.argv) < 2:
    print("Check Input: py -3 " + sys.argv[0] + " <url>")
    sys.exit(1)

# printing response from GET request
request = requests.get("https://"+sys.argv[1])
print("\n"+str(request.headers))

gethost = socket.gethostbyname(sys.argv[1])
print("\nThe IP address of "+sys.argv[1]+" is: "+gethost + "\n")

# use api for IP information requests --ipinfo.io in JSON

request_two = requests.get("https://ipinfo.io/"+gethost+"/json")
response = json.loads(request_two.text)

print("GPS Coordinates: "+response["loc"])
print("State: "+response["region"])
print("City/Town: "+response["city"])
print("Country: "+response["country"])
