#! python3

# converter.py - Converts filenames of images  in a directory such that they can be imported into Opentoonz as a single level.

import os, re

files = os.listdir()
dirName = os.path.basename(os.getcwd())
images = []

# TO-DO: Check filenames for images and stick them in a list
number_regex = re.compile(r'(\d)+.[png|jpg|tiff]')
for filename in files:
	mo = number_regex.search(filename)
	if mo.group(0) is not '':
		newname = dirName + '.' + ('0' * (4 - len(mo.group(1)))) + mo.group(1) + '.' + mo.group(2)
		os.rename(filename, newname)
	

# TO-DO: Convert image filenames

