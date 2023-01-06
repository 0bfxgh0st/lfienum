Local File Inclusion Enumeration (PoC)  

Almost whole system enumeration when target is vulnerable to LFI.  

```
Local File Inclusion Enumerator v1.0 by 0bfxgh0st*
Usage python3 lfienum <url> <option>

Options:

    --pids <n>                 Bruteforce process id's from 0 to <n> (/proc/<n>/cmdline) [default is set to 999]
    --pid  <n>                 Show single process id
    --fd   <n>                 Bruteforce file descriptors from 0 to <n> (/proc/self/fd/<n>) [default is set to 30]
    --wrapper <file>           Extract/decode hidden file using a wrapper (php://filter/convert.base64-encode/resource=)
    -w  or --wordlist          Use a custom wordlist
    -k  or --key               Extract id_rsa key
    -h  or --help              Show help panel
    -ah or --advanced-help     Show advanced help panel

Last positional argument:

    -vvv                       Show package info
    --only-url                 Dump urls only
```
