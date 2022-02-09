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
os.system("sudo usermod -aG gvm $USER; mkdir -p " + SOURCE_DIR)
os.system("mkdir -p " + BUILD_DIR)
os.system("mkdir -p " + INSTALL_DIR)
os.system("sudo apt update; sudo apt install --no-install-recommends --assume-yes build-essential curl cmake pkg-config python3-pip gnupg")
os.system("curl -O https://www.greenbone.net/GBCommunitySigningKey.asc; gpg --import GBCommunitySigningKey.asc")
wait = input("I am about to import a gpg key for GVM, please enter trust in the gpg environment, then enter '5' to trust fully. Enter 'quit' and run part 2 of the script")
os.system("gpg --edit-key 9823FAA60ED1E580")

