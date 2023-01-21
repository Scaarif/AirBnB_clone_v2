#!/usr/bin/env bash
# Configure Nginx servers, preparing them for web_static deployment	
sudo apt-get -y update
sudo apt-get -y install nginx
mkdir -p data/web_static/releases/test/
mkdir -p data/web_static/shared/
echo "Holberton School" > data/web_static/releases/test/index.html
ln -sf data/web_static/releases/test/ data/web_static/current
sudo chown -R ubuntu:ubuntu data/
sudo sed -i '48i\ \tlocation /hbnb_static {\n\t\t alias data/web_static/current/;\n\t}\n' /etc/nginx/sites-available/default
sudo service nginx restart
exit 0


