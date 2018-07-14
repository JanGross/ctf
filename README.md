# Minzkrauts home-made CTF

## Requirements
 - NGINX
 - Python, Virtualenv  

Create and use python Virtualenv with Python 3  
`virtualenv -p python3 venv`  
`source venv/bin/activate`

Install all Python requirements with  
`pip install -r requirements.txt`

Move all NGINX configs to /etc/nginx/sites-avaliable and activate/symlink them.
## Platform API
Navigate into `ctf_platform`.  
Run `flask init-db` to initialize the database if neccessary.  
Start the Flask app with gunicorn using   `./start_api.sh`  
The API server will be listening on port `4910`  
Configure NGINX reverse proxy to point at `http://127.0.0.1:4910` 
## Letsencrypt certificates
Navigate to certbot location and create certificate files with
```
sudo ./certbot-auto certonly --webroot -w var/www/html -d ctf.minzkraut.com --non-interactive --agree-tos --email {email}
```
Renew certificates and reload nginx with
```
sudo ./certbot-auto renew --webroot -w /var/www/html --post-hook "service nginx reload"
```