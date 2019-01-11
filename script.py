#!/usr/bin/python
import certifi
from concurrent.futures import ThreadPoolExecutor, as_completed
import logging
import socket
import sys
import urllib3
from urlparse import urlsplit

#reading file passed through argument
def readFile(filename):
	try:
		urlList = open(filename, 'r')
		return urlList
	except IOError:
		print("Could not read file:", filename)
		sys.exit()
	return

#scanning for .git exposed happening here
def scanForVuln(url):

	#expecting .git/HEAD will be readble if the website is under git directory
	fullUrl = "{0}/.git/HEAD".format(url[:-1])
	agent = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:61.0) Gecko/20100101 Firefox/61.0'}

	httpsRequest = urllib3.PoolManager(cert_reqs='CERT_REQUIRED',ca_certs=certifi.where())
	#print(httpsRequest)
	timeout = urllib3.Timeout(connect=5.0, read=10.0)
	try:
		httpsResponse = httpsRequest.request('GET', fullUrl, headers=agent, timeout=timeout)
	except e as Error:
		print e

	print("TESTING: {0}".format(fullUrl))
	if (httpsResponse.data == "ref: refs/heads/master\n"):
		print ".git is Exposed for url {0}".format(url)
		print "---------------------------"
	else:
		print ".git is secure or not present\n"
		print "---------------------------"
		httpsResponse = None
    	return

	httpsResponse = None
	return

#using concurrency for huge input
def findGitHosting(urlList):
    with ThreadPoolExecutor(max_workers=100) as executor:
		results = executor.map(scanForVuln, urlList)



def main():
	if(len(sys.argv)!=2):
		print("Usage python git.py <filename>")
		return
	else:
		filename = sys.argv[1]
		urlList = readFile(filename)
		print ""
		findGitHosting(urlList)
		exit()

if __name__== "__main__":
    main()
