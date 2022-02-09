#!/usr/bin/env python3
from decouple import config
import os.path
import os
import subprocess
import re
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
os.system("sudo apt install -y libglib2.0-dev libgpgme-dev libgnutls28-dev uuid-dev libssh-gcrypt-dev libhiredis-dev libxml2-dev libpcap-dev libnet1-dev")
os.system("sudo apt install -y libldap2-dev libradcli-dev")
Astring = "https://github.com/greenbone/gvm-libs/archive/refs/tags/v" + GVM_LIBS + ".tar.gz"
print(Astring)
Bstring = "" + SOURCE_DIR + "/gvm-libs-" + GVM_LIBS + ".tar.gz"
print(Bstring)
Cstring = "https://github.com/greenbone/gvm-libs/releases/download/v" + GVM_LIBS + "/gvm-libs-" + GVM_LIBS + ".tar.gz.asc"
print(Cstring)
Dstring = Bstring + ".asc"
os.system("curl -f -L " + Astring + " -o " + Bstring)
os.system("curl -f -L " + Cstring + " -o " + Dstring)
os.system("gpg --verify " + Dstring + " " + Bstring)
os.system("tar -C " + SOURCE_DIR + " -xvzf " + Bstring)
pathstring = "" + BUILD_DIR + "/gvm-libs"
os.system("mkdir " + pathstring)
path = "./build/gvm-libs"
os.getcwd()
os.chdir(path)
os.getcwd()
#os.system("echo HOME=" + output.replace("b/home/", '/') + ">> .env")


