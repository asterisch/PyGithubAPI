# curl method
# curl -i -u asterisch -d '{"scopes": ["repo"], "auto_init": "True", "name": "Aristotle2", "private": "True", "description": "This is the second test repository"}' https://api.github.com/user/repos

import requests
from getpass import getpass
from sys import argv
from requests.auth import HTTPBasicAuth
#import json
argc=len(argv)
if (argc<2 or argc>3):
	print "Usage: "+argv[0]+" \"Username\""
	exit(21)
url='https://api.github.com/user/repos'

username=argv[1]
password=getpass()
auth=HTTPBasicAuth(username,password)


data={}
data["name"]=raw_input("Repo name: ")
data["description"]=raw_input("Repo description: ")
auto=raw_input("Auto Init (y/N): ")
if (auto == "y" or auto == "Y"):
	data['auto_init']='True'
private=raw_input("Private repo (y/N): ")
if (private == 'y' or private == 'Y'):
	data['private']='True'
res = requests.post(url,auth=auth,json=data)
if (res.status_code == 204):
	print res.headers
	print "==================DONE!==================="
else:
	print res.json()

