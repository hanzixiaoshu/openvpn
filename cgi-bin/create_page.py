#!/usr/bin/python

# -*- coding:utf-8 -*-

import sys
import os
import rlcompleter
import subprocess
import codecs
import time
import cgi
import cgitb

form = cgi.FieldStorage()

cert_name = form.getvalue('cert_name_in')
bind_ip = form.getvalue('bind_ip_in')
email_user = form.getvalue('email_user_in')
station_name = form.getvalue('station_name_in')


#sourcr vars and create cert
os.popen("cd /usr/share/easy-rsa/2.0 ;source ./vars; /usr/share/easy-rsa/2.0/create_cert.sh " + cert_name)
content = ("ifconfig-push " + bind_ip + " 255.255.255.0")
f = codecs.open('/etc/openvpn/staticclients/' + cert_name,'w','utf-8')
f.write(content)

#time.sleep(1)
#zip cert and send email
os.popen("cd /usr/share/easy-rsa/2.0/keys ; zip -r " + cert_name + ".zip " + cert_name + ".* ca.*")
os.popen("echo 'StationName : " + station_name + "\nCertName : " + cert_name + "\nBindIP : " + bind_ip + "\nHello,This annex 
provides Openvpn Cert !' | mutt -s 'OpenVPN Cert' " + email_user + " -a /usr/share/easy-rsa/2.0/keys/" + cert_name + ".zip")
time.sleep(2)
#delete cert.zip
os.popen("rm -rf /usr/share/easy-rsa/2.0/keys/" + cert_name + ".zip")

print "Content-Type: text/html; charset=UTF-8"
print ""
print "<html>"
print "<body>"
print "<h4>Station Name: %s</h4>" % (station_name)
print "<h4>Cert Name: %s</h4>" % (cert_name)
print "<h4>Bind &nbsp &nbsp &nbspIP: %s</h4>" % (bind_ip)
print "<h4>Email send success !</h4>"
print "<a href=\"http://10.10.1.144/16.html\"><h2>Go back to the previous page</h2></a>"
print "<a href=\"http://10.10.1.172/home.html\"><h2>Return home page</h2></a>"
print "</body>"
print "</html>"
