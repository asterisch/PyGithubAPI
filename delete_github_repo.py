import requests
from getpass import getpass
from sys import argv
from requests.auth import HTTPBasicAuth
argc=len(argv)
if (argc<3 or argc>3):
	print "Usage: "+argv[0]+" \"Username\""+" \"Repo name\""
	exit(21)
username=argv[1]
reponame=argv[2]
password=getpass()
url="https://api.github.com/repos/"+username+"/"+reponame
auth=HTTPBasicAuth(username,password)
res = requests.delete(url,auth=auth)
if (res.status_code == 204):
	print res.headers
        print "==================DONE!==================="
else:
	print res.json()

