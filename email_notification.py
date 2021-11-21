import smtplib, socket, sys
from datetime import datetime

smtp_server_domain_name = 'smtp.gmail.com'
smtp_server_port = 587

server_username = ''
server_password = ''
sender_address  = ''
recipient_list  = ['']

TO = recipient_list[0]
FROM = sender_address
SUBJECT = 'SSH Session Notification'

header = 'To: {}\nFrom: {}\nSubject: {}\n\n'.format(TO, FROM, SUBJECT)
body = f"""
Someone has logged into a system over SSH.

User:   {sys.argv[1]}
IP:     {sys.argv[2] if (sys.argv[2] != '::1') else 'localhost'}
Time:   {datetime.now()}
System: {socket.gethostname()}

Thanks,
{socket.gethostname()} auto-notifier

This is an automated incident report. Please do not reply.
"""

server = smtplib.SMTP(smtp_server_domain_name, smtp_server_port)
server.starttls()
server.login(server_username, server_password)

try:
   server.sendmail(sender_address, recipient_list, header + body)
   print("[INFO] A system administrator has been notified of this session.")
except:
   print("[INFO] Error: Automated notification has failed to send. Please contact your system administrator for assistance.")