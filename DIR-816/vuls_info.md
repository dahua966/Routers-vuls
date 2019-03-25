#### info of vulnerability
There is a approaches to get routers’ many information without unauthentication.When GET the pages(eg.version.asp) without login, the response will contain a js section directing you to the login page, like this
```
 top.location.href = "/dir_login.asp"; 
```

But we could delete this command and page will not be redirected to login page with a simple [proxy script](https://github.com/dahua966/Routers-vuls/blob/master/DIR-816/proxy.py). Then we could see all the pages of the manager panel(d_status.asp,version.asp,d_dhcptbl.asp,d_acl.asp,etc).

Vulnerable targets include but are not limited to the lastest firmware versions of DIR-816(A1-V1.06)
