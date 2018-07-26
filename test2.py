import os
import hashlib
import collections
photos = os.listdir('photo')
photos_md5 = []
for fname in photos:
	photos_md5.append([hashlib.md5(fname).hexdigest()])
number_of_photo = range(len(photos_md5))

print number_of_photo

for i in number_of_photo:
	dupes = ''
	for j in number_of_photo:
		if photos_md5[i] == photos_md5[j]:
			dupes = dupes + photos[j]
	if dupes == '':
		dupes = 'None'
	print photos[i]
	print 'Duplicates :' + dupes
#End