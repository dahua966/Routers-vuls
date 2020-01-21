#### Vulnerability Detail
There are several pages in TrendNet TEW-722BRM can be accessed without authorization, which could lead to the leak of vital private information.These pages are "status/status_statistic.shtml", "status/traffic_log.shtml", "status/status_vdsl_statistic.shtml". When processed, it exposes the statistic, traffic log and DSL statistic of router.

#### PoC
http://targetip/status/status_statistic.shtml

![poc](https://github.com/dahua966/Routers-vuls/blob/master/TEW-722BRM/status_statistic.jpg)

http://targetip/status/traffic_log.shtml

![poc](https://github.com/dahua966/Routers-vuls/blob/master/TEW-722BRM/traffic_log.jpg)

http://targetip/status/status_vdsl_statistic.shtml

![poc](https://github.com/dahua966/Routers-vuls/blob/master/TEW-722BRM/DSL_statistic.jpg)

A vulnerability is in the 'MNU_access_failure.htm' page of the Netgear DGN2200, version DGN2200-V1.0.0.58_7.0.57, which can allow a remote attacker to access this page without any authentication. 



#### Acknowledgement
Thanks to the partners who discovered the vulnerability together：

Wei Xie

Zhen-hua Wang

En-Ze Wang