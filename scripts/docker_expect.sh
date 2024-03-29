#!/usr/bin/expect -f
set timeout 5000
spawn /opt/mhn/install.sh
expect "Do you wish to run in Debug mode?: y/n"
send "DEBUG_MODE\r"
expect "Superuser email:"
send "SUPERUSER_EMAIL\r"
expect "Superuser password:"
send "SUPERUSER_PASSWORD\r"
expect "Superuser password: (again):"
send "SUPERUSER_PASSWORD\r"
expect "Server base url"
send "SERVER_BASE_URL\r"
expect "Honeymap url"
send "HONEYMAP_URL\r"
expect "Mail server address"
send "SMTP_HOST\r"
expect "Mail server port"
send "SMTP_PORT\r"
expect "Use TLS for email?: y/n"
send "SMTP_TLS\r"
expect "Use SSL for email?: y/n"
send "SMTP_SSL\r"
expect "Mail server username"
send "SMTP_USERNAME\r"
expect "Mail server password"
send "SMTP_PASSWORD\r"
expect "Mail default sender"
send "SMTP_SENDER\r"
expect "Path for log file"
send "MHN_LOG\r"
expect "Would you like to integrate with Splunk?"
send "n\r"
expect "Would you like to install ELK?"
send "n\r"
expect "Would you like to add MHN rules to UFW?"
send "n\r"
expect EOF