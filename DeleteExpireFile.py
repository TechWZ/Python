#!/usr/bin/python3

import os
import time

currentTime = time.time()
operation_dir='/DatabaseBackup/BackupSQL'
for path,subDirNames,fileNames in os.walk(operation_dir):
    for fileName in fileNames:
        filePath = os.path.join(path,fileName)
        fileCtime = os.stat(filePath).st_ctime
        if currentTime-fileCtime > 2419200:
            os.system("rm -f "+filePath)