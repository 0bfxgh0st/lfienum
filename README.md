Local File Inclusion Enumeration (PoC)  

Almost whole system enumeration when target is vulnerable to LFI.  

<pre>
Local File Inclusion Enumerator v1.0 by 0bfxgh0st*
Usage python3 lfienum &lturl> &ltoption>

Options:

    -X POST/GET                   Request method

    --pids &ltn>                    Bruteforce process id's from 0 to &ltn> (/proc/&ltn>/cmdline) [default is set to 999]
    --pid &ltn>                     Show single process id
    --fd &ltn>                      Bruteforce file descriptors from 0 to &ltn> (/proc/self/fd/&ltn>) [default is set to 30]
    --wrapper &ltfile>              Extract/decode hidden file using a wrapper (php://filter/convert.base64-encode/resource=)
    -w,  --wordlist &ltwordlist>    Use a custom wordlist
    -k,  --key                    Extract id_rsa key

    -h,  --help                   Show help panel
    -ah, --advanced-help          Show advanced help panel

    -v,  -vvv                     Show package info
    -ou, --only-url               Dump urls only

    -x1                           Use XCF_A function print all text between tags (default)
    -x2                           Use XCF_B function print all text that isn't between any tag
    -x3                           Use XCF_C function print content between specific tag
    -x4                           Use XCF_D function delete all content inside &lthtml> and &lt/html> tags
    --exclude &ltstring>            Exclude responses that contains given string

Enumeration modes:

    --data-mode &ltkey name>        Data mode (LFI enumeration via data key)
    --cookie-mode &ltkey name>      Cookie mode (LFI enumeration via cookie key)

Examples:

    python3 lfienum "http://ghost.server/index.php?page="
    python3 lfienum "http://ghost.server/" --cookie-mode session
    python3 lfienum "http://ghost.server/index.js" --data-mode file
</pre>
