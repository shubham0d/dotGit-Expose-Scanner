import sys
import socket
from concurrent.futures import ThreadPoolExecutor, as_completed
import urllib3
import certifi
try:
    from urllib.parse import urlsplit
except ImportError:
     from urlparse import urlsplit


def readFile(filename):
	try:
		url_list = open(filename, 'r')
		return url_list
	except IOError:
		print("Could not read file:", filename)
		sys.exit()


def scanForVuln(url):

	#lets remove http/https for now, we will add it below
	url.replace("http://","")
	url.replace("https://","")

	#expecting .git/HEAD will be readble if the website is under git directory
    fullUrlSecure = "https://{0}/.git/HEAD".format(url)
	fullUrl = "http://{0}/.git/HEAD".format(url)
    agent = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:61.0) Gecko/20100101 Firefox/61.0'}

    httpsRequest = urllib3.PoolManager(
        cert_reqs='CERT_REQUIRED',
        ca_certs=certifi.where()
    )
	httpRequest = urllib3.PoolManager()
    timeout = urllib3.Timeout(connect=5.0, read=10.0)

    r = httpRequest.request('GET', furl, headers=agent, timeout=timeout)
    print("TEST: {0}".format(furl))
    print type(r.data)
    a = r.data
    print a[0:10]
    if (a == "ref: refs/heads/master\n"):
        print "Git is visible"
    else:
        print "Git is not visible"
    r = None


def findGitHosting(urlList):
	with ThreadPoolExecutor(max_workers=100) as executor:
	          results = executor.map(scanForVuln, urlList)


def main():
	if(len(sys.argv)!=2):
		print("Usage python git.py <filename>")
		return
	else:
		filename = sys.argv[1]
		url_list = read_file(filename)
		git_hosted_directory = git_directory_hosted(url_list)
