#!/usr/bin/python

import sys
import os
import rlcompleter
import subprocess
import codecs
import cgi
import cgitb

form = cgi.FieldStorage()

cert_name = form.getvalue('cert_name_in')
#cert_name = 'llxx'
#abind_ip = form.getvalue('bind_ip_in')
bind_ip = "255.255.255.255"


#sourcr vars and create cert
#os.popen("cd /usr/share/easy-rsa/2.0 ;source ./vars; /usr/share/easy-rsa/2.0/create_cert.sh " + cert_name)
#subprocess.check_call(['/usr/share/easy-rsa/2.0/create_cert.sh', cert])

content = ("ifconfig-push " + bind_ip + " 255.255.255.0")
f = codecs.open('/etc/openvpn/staticclients/' + cert_name,'w','utf-8')
f.write(content)

print "Content-Type: text/html"
print ""
print "<h4>Cert Name :  %s</h4>" % (cert_name)
print "<h4>The certificate has been canceled !!!</h4>"
#print "<h4>Bind &nbsp &nbsp &nbspIP: %s</h4>" % (bind_ip)
