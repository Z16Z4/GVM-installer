#!/usr/bin/env python3
from decouple import config
import os 
PATH = config('PATH')
INSTALL_PREFIX = config('INSTALL_PREFIX')
SOURCE_DIR = config('SOURCE_DIR')
BUILD_DIR = config('BUILD_DIR')
INSTALL_DIR = config('INSTALL_DIR')
GVM_VERSION = config('GVM_VERSION')
GVM_LIBS = config('GVM_LIBS')
GVMD_VERSION = config('GVMD_VERSION')
GSA_VERSION = config('GSA_VERSION')
OPENVAS_SMB_VERSION = config('OPENVAS_SMB_VERSION')
OPENVAS_SCANNER_VERSION = config('OPENVAS_SCANNER_VERSION')
OSPD_VERSION = config('OSPD_VERSION')
OSPD_OPENVAS_VERSION = config('OSPD_OPENVAS_VERSION')
os.system("sudo apt install -y redis-server")
#redis server
os.system("sudo cp " + SOURCE_DIR + "/openvas-scanner-" + GVM_VERSION + "/config/redis-openvas.conf /etc/redis")
os.system("sudo chown redis:redis /etc/redis/redis-openvas.conf")
os.system("echo 'db_address = /run/redis-openvas/redis.sock' | sudo tee -a /etc/openvas/openvas.conf")
os.system("sudo systemctl start redis-server@openvas.service")
os.system("sudo systemctl enable redis-server@openvas.service")
os.system("sudo usermod -aG redis gvm")

#set permissons 
os.system("sudo chown -R gvm:gvm /var/lib/gvm;sudo chown -R gvm:gvm /var/lib/openvas;sudo chown -R gvm:gvm /var/log/gvm;sudo chown -R gvm:gvm /run/gvm;sudo chmod -R g+srw /var/lib/gvm;sudo chmod -R g+srw /var/lib/openvas;sudo chmod -R g+srw /var/log/gvm")
os.system("sudo chown gvm:gvm /usr/local/sbin/gvmd;sudo chmod 6750 /usr/local/sbin/gvmd")
os.system("sudo chown gvm:gvm /usr/local/bin/greenbone-nvt-sync;sudo chmod 740 /usr/local/sbin/greenbone-feed-sync;sudo chown gvm:gvm /usr/local/sbin/greenbone-*-sync;sudo chmod 740 /usr/local/sbin/greenbone-*-sync")

os.system("echo 'time to run some manual commands'")
os.system("cat ./manual-commands")



message = '''

sudo vim /etc/sudoers
or 
sudo visudo

entry -
%gvm ALL = NOPASSWD: /usr/local/sbin/openvas




#database
sudo systemctl start postgresql@12-main
sudo -u postgres bash
createuser -DRS gvm
createdb -O gvm gvmd
exit

sudo -u postgres bash
psql gvmd
create role dba with superuser noinherit;
grant dba to gvm;
create extension "uuid-ossp";
create extension "pgcrypto";
exit
exit

#set password
gvmd --create-user=admin --password=<password>


'''

print(message)