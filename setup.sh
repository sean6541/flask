#!/bin/bash

apt-get update
apt-get -y install lighttpd python3-pip
python3 -m pip install flask flup
cp -r ./data/* /
chmod -R 755 /cgiserver
service lighttpd restart
