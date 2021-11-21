# ssh-email-notifier
Notify a system-administrator whenever someone logs into a system over SSH

This script can be used to send an automated email whenever a user logs into a server over SSH. By default, the SMTP server is set for Gmail.

Start by adding the required email login details to the beginning of the script.

To run the script at the start of every SSH session, add it to your `/etc/ssh/sshrc` file:

```
python3 <path_to_script> $USER $SSH_CLIENT[0]
```
