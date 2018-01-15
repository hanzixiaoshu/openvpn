#!/usr/bin/expect -f

set vpn_cert [lindex $argv 0]
set path /usr/share/easy-rsa/2.0
spawn $path/build-key $vpn_cert
expect "*"
send "\r"
expect "*"
send "\r"
expect "*"
send "\r"
expect "*"
send "\r"
expect "*"
send "\r"
expect "*"
send "\r"
expect "*"
send "\r"
expect "*"
send "\r"
expect "*"
send "\r"
expect "*"
send "\r"
expect "*"
send "y\r"
expect "*"
send "y\r"
expect eof
exit
