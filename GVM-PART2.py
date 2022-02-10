#!/usr/bin/env python3
from pickle import BUILD
from decouple import config
import os.path
import os
import subprocess
import re
#Importing useful environment variables
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
#Preinstall needs 
os.system("sudo apt install -y libglib2.0-dev libgpgme-dev libgnutls28-dev uuid-dev libssh-gcrypt-dev libhiredis-dev libxml2-dev libpcap-dev libnet1-dev")
os.system("sudo apt install -y libldap2-dev libradcli-dev")
#GVM LIBS 
#Location of GVM LIBS
Astring = "https://github.com/greenbone/gvm-libs/archive/refs/tags/v" + GVM_LIBS + ".tar.gz"
print(Astring)
#Location where we want GVM LIBS
Bstring = "" + SOURCE_DIR + "/gvm-libs-" + GVM_LIBS + ".tar.gz"
print(Bstring)
#GPG key location
Cstring = "https://github.com/greenbone/gvm-libs/releases/download/v" + GVM_LIBS + "/gvm-libs-" + GVM_LIBS + ".tar.gz.asc"
print(Cstring)
# full file name of GPG key
Dstring = Bstring + ".asc"
#Get GVM Libs and output in location specified
os.system("curl -f -L " + Astring + " -o " + Bstring)
#Get GPG and output in location specified
os.system("curl -f -L " + Cstring + " -o " + Dstring)
#Verify GPG key 
os.system("gpg --verify " + Dstring + " " + Bstring)
#Unzip file into source dir
os.system("tar -C " + SOURCE_DIR + " -xvzf " + Bstring)
#making build directory
os.system("mkdir -p " + BUILD_DIR + "/gvm-libs")
#need the home environment
HOME = os.environ.get('HOME')
#to change directory
os.chdir(HOME + "/build/gvm-libs")
#is this the correct directory?
os.system("pwd")
#it is great, lets build it
os.system("cmake " + SOURCE_DIR + "/gvm-libs-" + GVM_LIBS + " -DCMAKE_INSTALL_PREFIX=" + INSTALL_PREFIX + " -DCMAKE_BUILD_TYPE=Release -DSYSCONFDIR=/etc -DLOCALSTATEDIR=/var -DGVM_PID_DIR=/run/gvm")
os.system("make -j$(nproc)")
#cleanup
os.system("make DESTDIR=" + INSTALL_DIR + " install")
os.system("sudo cp -rv " + INSTALL_DIR + "/* /")
os.system("rm -rf " + INSTALL_DIR + "/*")
#GVMD
#get prere
os.system("sudo apt install -y libglib2.0-dev libgnutls28-dev libpq-dev postgresql-server-dev-12 libical-dev xsltproc rsync")
os.system("sudo apt install -y --no-install-recommends texlive-latex-extra texlive-fonts-recommended xmlstarlet zip rpm fakeroot dpkg nsis gnupg gpgsm wget sshpass openssh-client socat snmp python3 smbclient python3-lxml  gnutls-bin xml-twig-tools")
Estring = "https://github.com/greenbone/gvmd/archive/refs/tags/v" + GVMD_VERSION + ".tar.gz"
print(Estring)
Fstring = "" + SOURCE_DIR + "/gvmd-" + GVMD_VERSION + ".tar.gz"
print(Fstring)
Gstring = "https://github.com/greenbone/gvmd/releases/download/v" + GVMD_VERSION + "/gvmd-" + GVMD_VERSION + ".tar.gz.asc"
print(Gstring)
Hstring = Fstring + ".asc"
os.system("curl -f -L " + Estring + " -o " + Fstring)
os.system("curl -f -L " + Gstring + " -o " + Hstring)
os.system("gpg --verify " + Hstring + " " + Fstring)
os.system("tar -C " + SOURCE_DIR + " -xvzf " + Fstring)
os.system("mkdir -p " + BUILD_DIR + "/gvmd")
HOME = os.environ.get('HOME')
os.chdir(HOME + "/build/gvmd")
os.system("pwd")
os.system("cmake " + SOURCE_DIR + "/gvmd-" + GVMD_VERSION + " -DCMAKE_INSTALL_PREFIX=" + INSTALL_PREFIX + " -DCMAKE_BUILD_TYPE=Release -DLOCALSTATEDIR=/var -DSYSCONFDIR=/etc -DGVM_DATA_DIR=/var -DGVM_RUN_DIR=/run/gvm -DOPENVAS_DEFAULT_SOCKET=/run/ospd/ospd-openvas.sock -DGVM_FEED_LOCK_PATH=/var/lib/gvm/feed-update.lock -DSYSTEM_SERVICE_DIR=/lib/systemd/system -DDEFAULT_CONFIG_DIR=/etc/default -DLOGROTATE_DIR=/etc/logrotate.d")
os.system("make -j$(nproc)")
os.system("make DESTDIR=" + INSTALL_DIR + " install")
os.system("sudo cp -rv " + INSTALL_DIR + "/* /")
os.system("rm -rf " + INSTALL_DIR + "/*")
#GSA
os.system("sudo apt install -y libmicrohttpd-dev libxml2-dev libglib2.0-dev libgnutls28-dev")
os.system("sudo apt install -y nodejs")
os.system("curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | sudo apt-key add -")
os.system("sudo echo 'deb https://dl.yarnpkg.com/debian/ stable main' | sudo tee /etc/apt/sources.list.d/yarn.list")
os.system("sudo apt update;sudo apt install yarn -y;sudo yarn install;sudo yarn upgrade;yarn install;yarn upgrade;sudo apt install npm -y;npx browserslist@latest --update-db")
Istring = "https://github.com/greenbone/gsa/archive/refs/tags/v" + GSA_VERSION + ".tar.gz"
print(Istring)
Jstring = "" + SOURCE_DIR + "/gsa-" + GSA_VERSION + ".tar.gz"
print(Jstring)
Kstring = "https://github.com/greenbone/gsa/releases/download/v" + GSA_VERSION + "/gsa-" + GSA_VERSION + ".tar.gz.asc"
print(Kstring)
Lstring = Jstring + ".asc"
os.system("curl -f -L " + Istring + " -o " + Jstring)
os.system("curl -f -L " + Kstring + " -o " + Lstring)
os.system("gpg --verify " + Lstring + " " + Jstring)
os.system("tar -C " + SOURCE_DIR + " -xvzf " + Jstring)
os.system("mkdir -p " + BUILD_DIR + "/gsa")
HOME = os.environ.get('HOME')
os.chdir(HOME + "/build/gsa")
os.system("pwd")
os.system("cmake " + SOURCE_DIR + "/gsa-" + GSA_VERSION + " -DCMAKE_INSTALL_PREFIX=" + INSTALL_PREFIX + " -DCMAKE_BUILD_TYPE=Release -DSYSCONFDIR=/etc -DLOCALSTATEDIR=/var -DGVM_RUN_DIR=/run/gvm -DGSAD_PID_DIR=/run/gvm -DLOGROTATE_DIR=/etc/logrotate.d")
os.system("make -j$(nproc)")
os.system("make DESTDIR=" + INSTALL_DIR + " install")
os.system("sudo cp -rv " + INSTALL_DIR + "/* /")
os.system("rm -rf " + INSTALL_DIR + "/*")
#openvas smb 
os.system("sudo apt install -y gcc-mingw-w64 libgnutls28-dev libglib2.0-dev libpopt-dev libunistring-dev heimdal-dev perl-base")
Mstring = "https://github.com/greenbone/openvas-smb/archive/refs/tags/v" + OPENVAS_SMB_VERSION + ".tar.gz"
print(Mstring)
Nstring = "" + SOURCE_DIR + "/openvas-smb-" + OPENVAS_SMB_VERSION + ".tar.gz"
print(Nstring)
Ostring = "https://github.com/greenbone/openvas-smb/releases/download/v" + OPENVAS_SMB_VERSION + "/openvas-smb-" + OPENVAS_SMB_VERSION + ".tar.gz.asc"
print(Ostring)
Pstring = Nstring + ".asc"
os.system("curl -f -L " + Mstring + " -o " + Nstring)
os.system("curl -f -L " + Ostring + " -o " + Pstring)
os.system("gpg --verify " + Pstring + " " + Nstring)
os.system("tar -C " + SOURCE_DIR + " -xvzf " + Nstring)
os.system("mkdir -p " + BUILD_DIR + "/openvas-smb")
HOME = os.environ.get('HOME')
os.chdir(HOME + "/build/openvas-smb")
os.system("cmake " + SOURCE_DIR + "/openvas-smb-" + OPENVAS_SMB_VERSION + " -DCMAKE_INSTALL_PREFIX=" + INSTALL_PREFIX + " -DCMAKE_BUILD_TYPE=Release")
os.system("make -j$(nproc)")
os.system("make DESTDIR=" + INSTALL_DIR + " install")
os.system("sudo cp -rv " + INSTALL_DIR + "/* /")
os.system("rm -rf " + INSTALL_DIR + "/*")
#openvas scanner
os.system("sudo apt install -y bison libglib2.0-dev libgnutls28-dev libgcrypt20-dev libpcap-dev libgpgme-dev libksba-dev rsync nmap")
os.system("sudo apt install -y python-impacket")
os.system("pip3 install impacket; pip install impacket; sudo pip3 install impacket; pip install impacket")
os.system("sudo apt install libsnmp-dev")
Qstring = "https://github.com/greenbone/openvas-scanner/archive/refs/tags/v" + OPENVAS_SCANNER_VERSION + ".tar.gz"
print(Qstring)
Rstring = "" + SOURCE_DIR + "/openvas-scanner-" + OPENVAS_SCANNER_VERSION + ".tar.gz"
print(Rstring)
Sstring = "https://github.com/greenbone/openvas-scanner/releases/download/v" + OPENVAS_SCANNER_VERSION + "/openvas-scanner-" + OPENVAS_SCANNER_VERSION + ".tar.gz.asc"
print(Sstring)
Tstring = Rstring + ".asc"
os.system("curl -f -L " + Qstring + " -o " + Rstring)
os.system("curl -f -L " + Sstring + " -o " + Tstring)
os.system("gpg --verify " + Tstring + " " + Rstring)
os.system("tar -C " + SOURCE_DIR + " -xvzf " + Rstring)
os.system("mkdir -p " + BUILD_DIR + "/openvas-scanner")
HOME = os.environ.get('HOME')
os.chdir(HOME + "/build/openvas-scanner")
os.system("cmake " + SOURCE_DIR + "/openvas-scanner-" + OPENVAS_SCANNER_VERSION + " -DCMAKE_INSTALL_PREFIX=" + INSTALL_PREFIX + " -DCMAKE_BUILD_TYPE=Release -DSYSCONFDIR=/etc -DLOCALSTATEDIR=/var -DOPENVAS_FEED_LOCK_PATH=/var/lib/openvas/feed-update.lock -DOPENVAS_RUN_DIR=/run/ospd")
os.system("make -j$(nproc)")
os.system("make DESTDIR=" + INSTALL_DIR + " install")
os.system("sudo cp -rv " + INSTALL_DIR + "/* /")
os.system("rm -rf " + INSTALL_DIR + "/*")
#ospd-openvas
#get prere
os.system("sudo apt install -y python3 python3-pip python3-setuptools python3-packaging python3-wrapt python3-cffi python3-psutil python3-lxml python3-defusedxml python3-paramiko python3-redis")
#link to tar
Ustring = "https://github.com/greenbone/ospd/archive/refs/tags/v" + OSPD_VERSION + ".tar.gz"
print(Ustring)
#path where tar will be saved
HOME = os.environ.get('HOME')
Vstring = "" + HOME + "/source/ospd-" + OSPD_VERSION + ".tar.gz"
print(Vstring)
#path to gpg key 
Wstring = "https://github.com/greenbone/ospd/releases/download/v" + OSPD_VERSION + "/ospd-" + OSPD_VERSION + ".tar.gz.asc"
#file name of gpg key 
Xstring = Vstring + ".asc"
#get ospd-openvas
#get tar save as tar path
os.system("curl -f -L " + Ustring + " -o " + Vstring)
#get gpg key output as file name 
os.system("curl -f -L " + Wstring + " -o " + Xstring)
#verify file 
os.system("gpg --verify " + Xstring + " " + Vstring)
Ystring = "https://github.com/greenbone/ospd-openvas/archive/refs/tags/v" + OSPD_OPENVAS_VERSION + ".tar.gz"
print(Ystring)
HOME = os.environ.get('HOME')
Ytwo = "" + HOME + "/source/ospd-openvas-" + OSPD_OPENVAS_VERSION + ".tar.gz"
print(Ytwo)
Zstring = "https://github.com/greenbone/ospd-openvas/releases/download/v" + OSPD_OPENVAS_VERSION + "/ospd-openvas-" + OSPD_OPENVAS_VERSION + ".tar.gz.asc"
print(Zstring)
Ztwo = Ytwo + ".asc"
#get ospd-openvas sources
os.system("curl -f -L " + Ystring + " -o " + Ytwo)
os.system("curl -f -L " + Zstring + " -o " + Ztwo)
os.system("gpg -verify " + Ztwo + " " + Ytwo)
os.system("tar -C " + SOURCE_DIR + " -xvzf " + Vstring)
os.system("tar -C " + SOURCE_DIR + " -xvzf " + Ytwo)
HOME = os.environ.get('HOME')
os.chdir(HOME + "/source/ospd-" + OSPD_VERSION)
os.system("python3 -m pip install . --prefix=" + INSTALL_PREFIX + " --root=" + INSTALL_DIR)
HOME = os.environ.get('HOME')
os.chdir(HOME + "/source/ospd-openvas-" + OSPD_OPENVAS_VERSION)
os.system("python3 -m pip install . --prefix=" + INSTALL_PREFIX + " --root=" + INSTALL_DIR + " --no-warn-script-location")
os.system("sudo cp -rv" + INSTALL_DIR + "/* /")
os.system("rm -rf " + INSTALL_DIR + "/* /")
os.system("sudo apt install -y python3 python3-pip python3-setuptools python3-packaging python3-lxml python3-defusedxml python3-paramiko")
os.system("python3 -m pip install --user gvm-tools")
os.system("python3 -m pip install --prefix=" + INSTALL_PREFIX + " --root=" + INSTALL_DIR + " --no-warn-script-location gvm-tools")
os.system("sudo cp -rv " + INSTALL_DIR + "/* /")
os.system("rm -rf " + INSTALL_DIR + "/*")
