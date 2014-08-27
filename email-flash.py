#!/usr/bin/python3
import RPi.GPIO as GPIO
import feedparser
import time
import urllib
import getpass


#setup GPIO
GPIO.setmode(GPIO.BCM)
led_green = 18
led_red = 22
GPIO.setup(led_green,GPIO.OUT)
GPIO.setup(led_red,GPIO.OUT)

newmailthresh=0
nprev=0

USER=""
PASSWORD=""
if USER=="":
    USER = input('Gmail user name (up to the @gmail.com): ')
if PASSWORD=="":
    print('password for user ' + USER)
    PASSWORD = getpass.getpass()

while True:    

    pwdmgr = urllib.request.HTTPPasswordMgrWithDefaultRealm()
    pwdmgr.add_password("New mail feed", 'http://mail.google.com/', USER, PASSWORD)
    auth = urllib.request.HTTPBasicAuthHandler(pwdmgr)
    opener = urllib.request.build_opener(auth)
    data = opener.open('http://mail.google.com/mail/feed/atom')
    d = feedparser.parse(data)
    print( d.feed.title )
    n = int(d.feed.fullcount)
    print(str(n) + " new mails (previously " + str(nprev) + ")")
#newmails = int(feedparser.parse("https://" + USER + ":" + PASSWORD +"@mail.google.com/gmail/feed/atom")["feed"]["fullcount"])   
    if n > newmailthresh:
        GPIO.output(led_green,1)
    else:
        GPIO.output(led_green,0)
    if n > nprev:
        GPIO.output(led_red,1)
    else:
        GPIO.output(led_red,0)
    #sleep for 10s, flash as an option
    if n > nprev:
        count = 0
        while count<5:
            time.sleep(1)
            GPIO.output(led_red,0)
            time.sleep(1)
            GPIO.output(led_red,1)
            count=count+1
    else:
        time.sleep(10)
    nprev = n

    

print("Done")

