import os
import hashlib
photos = os.listdir('photo')
photos_with_md5 = {}
for fname in photos:
	photos_with_md5[fname] = hashlib.md5(fname).digest())
print photos_with_md5

