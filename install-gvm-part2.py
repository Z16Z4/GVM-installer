#!/usr/bin/env python3 

import os 

os.system('''sudo sed -i 's/\"$/\:\/opt\/gvm\/bin\:\/opt\/gvm\/sbin\:\/opt\/gvm\/\.local\/bin\"/g' /etc/environment''')
os.system('sudo echo "/opt/gvm/lib" > /etc/ld.so.conf.d/gvm.conf')
