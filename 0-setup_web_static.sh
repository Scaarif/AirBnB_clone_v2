#!/usr/bin/env bash
# Sets up your web servers for deployment of 'web_static' by:
# 	installing Nginx if not already installed
#	creating folders /data/web_static/releases/test &  /data/web_static/shared if they don't already exist
#	creating a HTML file /data/web_static/releases/test/index.html with simple content to test configuration
# 	creating a symbolic link /data/web_static/current linked to /data/web_static/releases/test folder
#	(if the symbolic exists it should be deleted and recreated every time the script is ran)
#	give ownership of the /data/ folder (and all its contents) to the 'ubuntu' user AND group
#	update the Nginx configuration to server the content of /data/web_sttaic/current/ to 'hbnb_static' eg
# (ex. https://mydomainname.tech/hbnb_static) use alias inside Nginx configuration...
#	Resttart Nginx after updating the config... 

# check that nginx is installed
installed=$(sudo apt-mark showinstall | grep "nginx" &> /dev/null; echo $?)
if [ "$installed" -ne 0 ]
then
	sudo apt-get -y update
	sudo apt-get -y install nginx
fi
# create the folders needed (/data/ folders)
mkdir -p ~/data/web_static/releases/test/
mkdir -p ~/data/web_static/shared/
# create a HTML file with simple content to test configuration
echo "Hello Rahab!" > data/web_static/releases/test/index.html
# create a symbolic link (/data/web_static/current) to /data/web_static/releases/test/ (replace it if it alraedy exists)
ln -sf ~/data/web_static/releases/test/ ~/data/web_static/current
# give ownership of the /data/folder and its contents to 'ubuntu' owner and group
sudo chown -R ubuntu:ubuntu ~/data/
# configure Nginx to serve the contents of /data/web_static/current to 'hbnb_static' (eg https://mydomain.tech/hbnb_static ) . use ALIAS inside the configuration
sudo sed -i '48i\ \tlocation /hbnb_static {\n\t\t alias /data/web_static/current/;\n\t}\n' /etc/nginx/sites-available/default
# restart nginx after updating the configuration
sudo service nginx restart
# exit successfully (always)
exit 0


