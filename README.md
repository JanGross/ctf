# Minzkrauts home-made CTF

## Letsencrypt certificates
Navigate to certbot location and create certificate files with
```
sudo ./certbot-auto certonly --webroot -w var/www/html -d ctf.minzkraut.com --non-interactive --agree-tos --email {email}
```
Renew certificates and reload nginx with
```
sudo ./certbot-auto renew --webroot -w /var/www/html --post-hook "service nginx reload"
```