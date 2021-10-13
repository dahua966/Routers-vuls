#### Vulnerability Information
There are some web interfaces without authentication requirements on D-Link DIR-868L B1-2.03 and DIR-817LW A1-1.04 routers. An attacker can get the router's username and password (and other information) via a DEVICE.ACCOUNT value for SERVICES in conjunction with AUTHORIZED_GROUP=1%0a to getcfg.php. This could be used to control the router remotely.

####  CVE ID 
CVE-2019-17505