import os
import hashlib
import collections
photos = os.listdir('photo')
photos_md5 = []
for fname in photos:
	photos_md5 = photos_md5 + hashlib.md5(fname).hexdigest()
print photos_md5
for index in range(len(photos_md5)):
	if photos_md5[index].count(l) = 1:
		print photos[index]
		print 'Duplicates : None'
	else:
		print 'Duplicates :'
		for ind in range(len(photos_md5)):
			if photos_md5[index]=photos_md5[ind]:
				print photos[ind]
