import os
import hashlib
import collections

photos = os.listdir('photo')

def md5(fname):
    hash_md5 = hashlib.md5()
    with open(fname, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()

photos_md5 = []
for f in photos:
	photos_md5.append(md5(f))
number_of_photo = range(len(photos_md5))


for i in number_of_photo:
	dupes = ''
	for j in number_of_photo:
		if photos_md5[i] == photos_md5[j] and i != j:
			dupes = dupes + photos[j]
	if dupes == '':
		dupes = 'None'
	print photos[i]
	print 'Duplicates :' + dupes
#End