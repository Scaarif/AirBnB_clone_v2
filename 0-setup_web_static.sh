#!/usr/bin/env bash
# Configure Nginx servers, preparing them for web_static deployment

# update and install necessary packages
apt-get -y update
apt-get -y install nginx
# create the required repos
mkdir -p /data/web_static/releases/test/
mkdir -p /data/web_static/shared/
# add an index.html file (for testing)
echo "Holberton School" > /data/web_static/releases/test/index.html
# add a symbolic link
ln -sf /data/web_static/releases/test/ /data/web_static/current
# change the ownership of /data/ folder
chown -R ubuntu:ubuntu /data/
# configure nginx to serve requests from uri/hbnb_static/
sed -i '40i\\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n' /etc/nginx/sites-available/default
# restart nginx for configurations to update/apply
service nginx restart
# always exit successfully
exit 0


