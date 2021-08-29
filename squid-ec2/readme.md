### SQUID PROXY

commands to setup a AWS EC2 instance running a Squid proxy with basic user/password authentication

To create the password file with your own user/passord please go to:
https://veesp.com/blog/squid-authentication/

Userful commands

```
sudo yum install squid
sudo cp squid.conf /etc/squid/squid.conf
sudo cp passwords /etc/squid/
sudo service squid restart
sudo systemctl enable squid
sudo systemctl is-enabled squid
```	

Once running
```	
aws ec2 stop-instances --instance-ids i-0a2bccb31aa5c1f25
aws ec2 describe-instance-status --instance-ids i-0a2bccb31aa5c1f25
aws ec2 start-instances --instance-ids i-0a2bccb31aa5c1f25
aws ec2 describe-instances --instance-ids i-0a2bccb31aa5c1f25 --query "Reservations[*].Instances[*].{DNS:PublicDnsName,IP:PublicIpAddress}" --output=text
aws ec2 reboot-instances --instance-ids i-0a2bccb31aa5c1f25
```	
