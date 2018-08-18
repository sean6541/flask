#!/bin/bash

apt-get update
apt-get -y install apache2 libapache2-mod-xsendfile libapache2-mod-wsgi-py3 python3-pip
python3 -m pip install flask flup
cp -r ./data/* /
chmod -R 755 /cgiserver
a2dissite 000-default
a2ensite cgiserver
service apache2 restart
