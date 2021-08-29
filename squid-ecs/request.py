import requests

proxy_dns = "kadriand:shirohige@54.90.5.224:3128"
# proxy_dns = "kadriand:shirohige@squid-proxy-loadbalancer-793568071.us-east-1.elb.amazonaws.com:80"
http_proxy  = f"http://{proxy_dns}"
https_proxy = f"https://{proxy_dns}"
ftp_proxy   = f"ftp://{proxy_dns}"

proxyDict = { 
              "http"  : http_proxy, 
              "https" : https_proxy, 
              "ftp"   : ftp_proxy
            }

r = requests.get('https://www.google.com', proxies=proxyDict)
print(r.text)