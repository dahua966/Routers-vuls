### RCE vulnerability in D-Link
In file `/etc/services/DEVICE.TIME.php`,
```
   163	$enable = query("/device/time/ntp/enable");
   164	if($enable=="") $enable = 0;
   165	$enablev6 = query("/device/time/ntp6/enable");
   166	if($enablev6=="") $enablev6 = 0;
   167	$server = query("/device/time/ntp/server");
   ...
   172	if ($enable==1 && $enablev6==1)
   ...
   184				'SERVER4='.$server.'\n'.
   ...
   189				'	ntpclient -h $SERVER4 -i 5 -s -4 > /dev/console\n'.
```

The $SERVER variable is spliced into the string of the command execution, resulting in command injection. So atacker could inject arbitrary code into the string and execute it. The exploit script is exp.py. 
#### Acknowledgement
Thanks to the partners who discovered the vulnerability together：

Wei Xie

Zhen-hua Wang

En-Ze Wang
