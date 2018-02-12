#!/usr/bin/env python
import shutil

with open ('HostsCopyFull.txt', 'r') as f:
	for line in f:
		filename = line.rstrip()
		try:
			shutil.copy2(filename,'/home/divyae/divyae2/HOSTS/UniqueIdentifiers/6Feb/')
                except shutil.Error:
			pass




