#!/usr/bin/env bash
# Configure Nginx servers, preparing them for web_static deployment	
apt-get -y update
apt-get -y install nginx
service nginx start
mkdir -p /data/web_static/releases/test/
mkdir -p /data/web_static/shared/
echo "Holberton School" > /data/web_static/releases/test/index.html
ln -sf /data/web_static/releases/test/ /data/web_static/current
chown -R ubuntu:ubuntu /data/
sed -i '48i\\tlocation /hbnb_static/ {\n\t\t alias data/web_static/current/;\n\t}\n' /etc/nginx/sites-available/default
service nginx restart
exit 0


