import urllib2

import cookielib
from getpass import getpass
username="9503656659"
password="9503656659"
msg="hello MIT"
number=["8329617563"]
#msg="+".join(msg.split(' '))
print msg
print "entered to send"
url = 'http://site24.way2sms.com/Login1.action?'
data = 'username='+username+'&password='+password+'&Submit=Sign+in'
cj = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
opener.addheaders = [('User-Agent','Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.120 Safari/537.36')]
try:
    usock=opener.open(url,data)
except IOError:
    print "error while login"
for i in number:
    jession_id = str(cj).split('~')[1].split(' ')[0]
    send_sms_url = 'http://site24.way2sms.com/smstoss.action?'
    send_sms_data = 'ssaction=ss&Token='+jession_id+'&mobile='+i+'&message='+msg+'&msgLen=136'
    opener.addheaders = [('Referer', 'http://site25.way2sms.com/sendSMS?Token='+jession_id)]
    try:
        sms_sent_page = opener.open(send_sms_url,send_sms_data)
    except IOError:
        print "Error while sending message"
    print "SMS has been sent."
