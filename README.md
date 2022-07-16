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

Internal wordlist from sources:  
https://github.com/danielmiessler/SecLists/blob/master/Fuzzing/LFI/LFI-gracefulsecurity-linux.txt  
https://github.com/danielmiessler/SecLists/blob/master/Fuzzing/LFI/LFI-gracefulsecurity-windows.txt  
