#!/usr/bin/python

import os
import os.path
import time
import tarfile
import sys

current_time = time.time()

source = '/home/user-3/folder/'
mydir = '/home/user-3/backup-py/'
targetBackup = mydir + time.strftime('%Y%m%d%H%M%S') + '.tar.gz'

files = os.listdir(mydir)

files = [os.path.join(mydir, file) for file in files]

tar = tarfile.open(targetBackup, "w:gz")
tar.add(source)
tar.close()
#print(files)
#print(len(files))
if len(files) >= 7:
    files = [file for file in files if os.path.isfile(file)]
    #print(files)
    oldest_file = min(files, key=os.path.getctime)
    #print(oldest_file)
    os.remove(oldest_file)
