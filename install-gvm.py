#!/usr/bin/env python3 

import os 

#Update system
os.system("sudo apt-get update;sudo apt-get upgrade; sudo apt update; sudo apt upgrade")

#Install required packages as root
os.system("sudo apt-get -y install gcc g++ make bison flex libksba-dev curl redis libpcap-dev cmake git pkg-config libglib2.0-dev libgpgme-dev libgnutls28-dev uuid-dev libssh-gcrypt-dev libldap2-dev gnutls-bin libmicrohttpd-dev libhiredis-dev zlib1g-dev libxml2-dev libradcli-dev libldap2-dev doxygen nmap gcc-mingw-w64 xml-twig-tools libical-dev perl-base heimdal-dev libpopt-dev libsnmp-dev python3-setuptools python3-paramiko python3-lxml python3-defusedxml python3-dev gettext python3-polib xmltoman python3-pip texlive-fonts-recommended xsltproc texlive-latex-extra rsync ufw ntp libunistring-dev git libnet1-dev graphviz graphviz-dev --no-install-recommends")

#Update system
os.system("sudo curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | sudo apt-key add -")
os.system('''sudo echo "deb https://dl.yarnpkg.com/debian/ stable main" | sudo tee /etc/apt/sources.list.d/yarn.list''')
os.system("sudo apt update")

#Install yarn as root
os.system("sudo apt install yarn -y; sudo yarn install; sudo yarn upgrade")

#Get postgresql
os.system("sudo apt-get -y install postgresql postgresql-contrib postgresql-server-dev-all")
os.system("sudo systemctl restart postgresql")

#Add gvm user 
os.system('''sudo useradd -r -d /opt/gvm -c "GVM (OpenVAS) User" -s /bin/bash gvm''')
os.system("sudo mkdir /opt/gvm")
os.system("sudo chown gvm:gvm /opt/gvm")

#As user setup postgresql 
os.system("sudo -Hiu postgres createuser gvm")
os.system("sudo -Hiu postgres createdb -O gvm gvmd")
os.system("sudo -Hiu postgres psql -c 'create role dba with superuser noinherit;' gvmd")
os.system("sudo -Hiu postgres psql -c 'grant dba to gvm;' gvmd")
os.system('''sudo -Hiu postgres psql -c 'create extension "uuid-ossp";' gvmd''')
os.system('''sudo -Hiu postgres psql -c 'create extension "pgcrypto";' gvmd''')
os.system("systemctl restart postgresql")
os.system("sudo systemctl restart postgresql")
os.system("systemctl enable postgresql")
os.system("sudo systemctl enable postgresql")
os.system("sudo cp -r install-gvm-part2.py /opt/gvm")
# As root
os.system("echo 'IMPORTANT:'")
os.system("echo ""Please enter 'sudo su - gvm '  and run the nex installer""")


