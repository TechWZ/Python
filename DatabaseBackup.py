#!/usr/bin/python3

import time
import os

time_str=time.strftime("%Y%m%d%H%M%S",time.localtime())

bashCommand = 'mysqldump -h2402:f000:1:9e1::9:248 -unidtga -pNIDTGA_802.1x campus6 > /DatabaseBackup/BackupSQL/campus6_'+time_str+'_backup.sql'
os.system(bashCommand)
