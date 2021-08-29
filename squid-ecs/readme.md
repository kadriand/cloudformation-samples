## SQUID PROXY

Check
apache2-utils 
https://veesp.com/blog/squid-authentication/

### Build Image
```bash

docker build -t squid-proxy .
docker run -p 3128:3128 squid-proxy
docker tag squid-proxy kadriand/squid-proxy:latest
docker push kadriand/squid-proxy:latest
```