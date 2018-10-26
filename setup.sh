#!/bin/bash

apt-get update
apt-get -y install python3 python3-flask apache2 libapache2-mod-wsgi-py3 libapache2-mod-xsendfile
cp -r ./data/* /
chmod -R 755 /var/www/cgiserver
a2dissite 000-default
a2ensite cgiserver
service apache2 restart
