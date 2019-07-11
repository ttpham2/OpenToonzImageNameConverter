#! python3

# converter.py - Converts filenames of images  in a directory such that they can be imported into Opentoonz as a single level.

import os, re, sys

if len(sys.argv) > 1:
	image_name = sys.argv[1]
files = os.listdir()
directory_name = os.path.basename(os.getcwd())
images = []

# TO-DO: Check filenames for images and stick them in a list
number_regex = re.compile(r'(\d{1,4}).(png|jpg|tiff)')
for filename in files:
	mo = number_regex.search(filename)
	if mo is not None:
		if len(sys.argv) > 1:
			newname = image_name + '.' + ('0' * (4 - len(mo.group(1)))) + mo.group(1) + '.' + mo.group(2)
		else:
			newname = directory_name + '.' + ('0' * (4 - len(mo.group(1)))) + mo.group(1) + '.' + mo.group(2)
		print('renaming ' + filename + ' to ' + newname)
		os.rename(filename, newname)
		
print("All found filenames converted")

